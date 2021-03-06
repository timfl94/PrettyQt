# -*- coding: utf-8 -*-
"""
@author: Philipp Temminghoff
"""

from typing import Union

from qtpy import QtWidgets

from prettyqt import widgets


QtWidgets.QMenuBar.__bases__ = (widgets.Widget,)


class MenuBar(QtWidgets.QMenuBar):

    def __add__(self, other):
        if isinstance(other, (QtWidgets.QAction, QtWidgets.QMenu)):
            self.add(other)
            return self

    def add_action(self, action: Union[QtWidgets.QAction, str]):
        if isinstance(action, str):
            action = widgets.Action(action)
            self.addAction(action)
            return action
        return self.addAction(action)

    def add_menu(self, menu: Union[QtWidgets.QMenu, str]):
        if isinstance(menu, str):
            menu = widgets.Menu(menu)
            self.addMenu(menu)
            return menu
        return self.addMenu(menu)

    def add(self, item):
        if isinstance(item, QtWidgets.QMenu):
            return self.add_menu(item)
        else:
            return self.add_action(item)


if __name__ == "__main__":
    app = widgets.app()
    win = QtWidgets.QMainWindow()
    menu_bar = MenuBar()
    act = menu_bar.add_menu("test")
    win.setMenuBar(menu_bar)
    win.show()
    app.exec_()
