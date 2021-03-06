# -*- coding: utf-8 -*-
"""
@author: Philipp Temminghoff
"""

from qtpy import QtWidgets

from prettyqt import widgets


QtWidgets.QMdiSubWindow.__bases__ = (widgets.Widget,)


class MdiSubWindow(QtWidgets.QMdiSubWindow):
    pass


if __name__ == "__main__":
    app = widgets.app()
    widget = MdiSubWindow()
    widget.show()
    app.exec_()
