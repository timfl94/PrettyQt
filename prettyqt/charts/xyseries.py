# -*- coding: utf-8 -*-
"""
@author: Philipp Temminghoff
"""

from qtpy.QtCharts import QtCharts
from prettyqt import charts

QtCharts.QXYSeries.__bases__ = (charts.AbstractSeries,)


class XYSeries(QtCharts.QXYSeries):

    """
    QXYSeries with some custom properties
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._process_name = ""

    def __getstate__(self):
        return dict(points=self.pointsVector())

    def __setstate__(self, state):
        self.__init__()
        super().append(state["points"])
