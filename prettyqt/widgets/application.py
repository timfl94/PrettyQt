# -*- coding: utf-8 -*-
"""
@author: Philipp Temminghoff
"""

import pathlib
import sys
from typing import Optional, Union

import qtawesome as qta
from qtpy import QtCore, QtWidgets, QtGui

from prettyqt import core, gui


QtWidgets.QApplication.__bases__ = (gui.GuiApplication,)


class Application(QtWidgets.QApplication):

    def set_icon(self, icon: Union[QtGui.QIcon, str, None]):
        """set the icon for the menu

        Args:
            icon: icon to use
        """
        if not icon:
            icon = gui.Icon()
        elif isinstance(icon, str):
            icon = qta.icon(icon, color="lightgray")
        self.setWindowIcon(icon)

    def load_language_file(self, path: pathlib.Path):
        translator = core.Translator(self)
        translator.load(str(path))
        self.installTranslator(translator)

    def set_metadata(self,
                     app_name: Optional[str] = None,
                     app_version: Optional[str] = None,
                     org_name: Optional[str] = None,
                     org_domain: Optional[str] = None):
        if app_name:
            self.setApplicationName(app_name)
        if app_version:
            self.setApplicationVersion(app_name)
        if org_name:
            self.setOrganizationName(org_name)
        if org_domain:
            self.setOrganizationDomain(org_domain)

    def main_loop(self):
        return self.exec_()

    @classmethod
    def use_hdpi_bitmaps(cls):
        cls.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps)

    @classmethod
    def disable_window_help_button(cls):
        cls.setAttribute(QtCore.Qt.AA_DisableWindowContextHelpButton)

    @classmethod
    def copy_to_clipboard(cls, text: str):
        """
        Sets clipboard to supplied text
        """
        cb = cls.clipboard()
        cb.clear(mode=cb.Clipboard)
        cb.setText(text, mode=cb.Clipboard)

    @classmethod
    def get_mainwindow(cls) -> Optional[QtWidgets.QMainWindow]:
        widget_list = cls.instance().topLevelWidgets()
        for widget in widget_list:
            if isinstance(widget, QtWidgets.QMainWindow):
                return widget
        return None

    @classmethod
    def create_default_app(cls) -> "Application":
        cls.disable_window_help_button()
        cls.use_hdpi_bitmaps()
        app = cls(sys.argv)
        return app
