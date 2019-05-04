# -*- coding: utf-8 -*-
"""
@author: Philipp Temminghoff
"""

from qtpy import QtGui


class Font(QtGui.QFont):

    def __getstate__(self):
        return dict(family=self.family(),
                    pointsize=self.pointSize(),
                    bold=self.bold(),
                    italic=self.italic())

    def __setstate__(self, state):
        super().__init__()
        self.setFamily(state["family"])
        if state["pointsize"] > -1:
            self.setPointSize(state["pointsize"])
        self.setBold(state["bold"])
        self.setItalic(state["italic"])

    def set_size(self, size: int):
        pass

    @classmethod
    def mono(cls, size=8):
        font = cls("Consolas", size)
        # font.setStyleHint()
        return font


if __name__ == "__main__":
    font = Font("Consolas")
