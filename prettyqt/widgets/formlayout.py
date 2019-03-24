# -*- coding: utf-8 -*-
"""
@author: Philipp Temminghoff
"""

from qtpy import QtWidgets

MODES = {"maximum": QtWidgets.QLayout.SetMaximumSize,
         "fixed": QtWidgets.QLayout.SetFixedSize}


class FormLayout(QtWidgets.QFormLayout):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_size_mode("maximum")
        self.setVerticalSpacing(8)

    def __getitem__(self, index):
        return self.itemAt(index)

    def set_size_mode(self, mode):
        self.setSizeConstraint(MODES[mode])

    def set_label_widget(self, row, widget):
        if isinstance(widget, str):
            widget = QtWidgets.QLabel(widget)
        self.setWidget(row, QtWidgets.QFormLayout.LabelRole, widget)

    def set_field_widget(self, row, widget):
        if isinstance(widget, str):
            widget = QtWidgets.QLabel(widget)
        self.setWidget(row, QtWidgets.QFormLayout.FieldRole, widget)

    def set_spanning_widget(self, row, widget):
        if isinstance(widget, str):
            widget = QtWidgets.QLabel(widget)
        self.setWidget(row, QtWidgets.QFormLayout.SpanningRole, widget)

    @classmethod
    def from_dict(cls, dct, parent=None):
        formlayout = FormLayout(parent)
        for i, (k, v) in enumerate(dct.items(), start=1):
            if k is not None:
                formlayout.set_label_widget(i, k)
            if v is not None:
                formlayout.set_field_widget(i, v)
        return formlayout