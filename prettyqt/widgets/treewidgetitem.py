# -*- coding: utf-8 -*-
"""
@author: Philipp Temminghoff
"""

from typing import Union

import qtawesome as qta
from qtpy import QtWidgets, QtCore, QtGui

from prettyqt import gui
from prettyqt.utils import bidict


STATES = bidict(unchecked=QtCore.Qt.Unchecked,
                partial=QtCore.Qt.PartiallyChecked,
                checked=QtCore.Qt.Checked)


class TreeWidgetItem(QtWidgets.QTreeWidgetItem):

    def __repr__(self):
        return f"TreeWidgetItem()"

    def __getstate__(self):
        return dict(text=self.text(),
                    tooltip=self.toolTip(),
                    statustip=self.statusTip(),
                    checkstate=self.get_checkstate(),
                    icon=gui.Icon(self.icon()) if not self.icon().isNull() else None,
                    data=self.data(QtCore.Qt.UserRole))

    def __setstate__(self, state):
        self.__init__()
        self.setText(state.get("text", ""))
        self.setToolTip(state.get("tooltip", ""))
        self.setStatusTip(state.get("statustip", ""))
        self.setData(QtCore.Qt.UserRole, state["data"])
        self.set_icon(state["icon"])
        self.set_checkstate(state["checkstate"])

    def set_icon(self, icon: Union[QtGui.QIcon, str, None]):
        """set the icon for the action

        Args:
            icon: icon to use
        """
        if not icon:
            icon = gui.Icon()
        elif isinstance(icon, str):
            icon = qta.icon(icon)
        self.setIcon(icon)

    def set_checkstate(self, state: str):
        """set checkstate of the checkbox

        valid values are: unchecked, partial, checked

        Args:
            state: checkstate to use

        Raises:
            ValueError: invalid checkstate
        """
        if state not in STATES:
            raise ValueError("Invalid checkstate.")
        self.setCheckState(STATES[state])

    def get_checkstate(self) -> str:
        """returns checkstate

        possible values are "unchecked", "partial", "checked"

        Returns:
            checkstate
        """
        return STATES.inv[self.checkState()]
