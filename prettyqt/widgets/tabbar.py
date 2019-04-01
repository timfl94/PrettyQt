# -*- coding: utf-8 -*-
"""
@author: Philipp Temminghoff
"""

from qtpy import QtWidgets, QtCore, QtGui

ELIDE_MODES = dict(left=QtCore.Qt.ElideLeft,
                   right=QtCore.Qt.ElideRight,
                   middle=QtCore.Qt.ElideMiddle,
                   none=QtCore.Qt.ElideNone)

SELECTION_MODES = dict(left=QtWidgets.QTabBar.SelectLeftTab,
                       right=QtWidgets.QTabBar.SelectRightTab,
                       previous=QtWidgets.QTabBar.SelectPreviousTab)


class TabBar(QtWidgets.QTabBar):
    on_detach = QtCore.Signal(int, QtCore.QPoint)

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setAcceptDrops(True)
        self.set_elide_mode("right")
        self.set_remove_behaviour("left_tab")
        self.mouse_cursor = QtGui.QCursor()

    #  Send the on_detach when a tab is double clicked
    def mouseDoubleClickEvent(self, event):
        event.accept()
        self.on_detach.emit(self.tabAt(event.pos()), self.mouse_cursor.pos())

    def set_remove_behaviour(self, mode):
        """sets the remove hehaviour

        What tab should be set as current when removeTab is called
        if the removed tab is also the current tab.
        Possible values: left, right, previous
        Args:
            mode: new remove behaviour
        """
        if mode not in SELECTION_MODES:
            raise ValueError("Mode not available")
        self.setSelectionBehaviorOnRemove(SELECTION_MODES[mode])

    def set_elide_mode(self, mode):
        if mode not in ELIDE_MODES:
            raise ValueError("Mode not available")
        self.setElideMode(ELIDE_MODES[mode])