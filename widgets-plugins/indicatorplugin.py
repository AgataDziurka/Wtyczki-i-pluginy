#!/usr/bin/python
# -*- coding: utf-8 -*-


from PyQt4 import QtCore, QtGui
from PyQt4.QtDesigner import QPyDesignerCustomWidgetPlugin

from indicatorwidget import IndicatorWidget

class IndicatorPlugin(QPyDesignerCustomWidgetPlugin):

    def __init__(self, parent=None):
        super(IndicatorPlugin, self).__init__(parent)

        self.initialized = False

    def initialize(self, core):
        if self.initialized:
            return

        self.initialized = True

    def isInitialized(self):
        return self.initialized

    def createWidget(self, parent):
        return IndicatorWidget(parent)

    def name(self):
        return "IndicatorWidget"

    def toolTip(self):
        return ""

    def whatsThis(self):
        return ""

    def isContainer(self):
        return False

    def includeFile(self):
        return "indicatorwidget"

    def group(self):
        return "Control and measurement"

    def icon(self):
        return QtGui.QIcon(_logo_pixmap)

_logo_16x16_xpm = [
"16 16 4 1",
"p c #ff8a22",
"s c #8e8e8e",
"# c #000000",
". c #ffffff",
"................",
"................",
"................",
"................",
"################",
"#sssppsssssssss#",
"#sssppsssssssss#",
"#sssppsssssssss#",
"#sssppsssssssss#",
"#sssppsssssssss#",
"#sssppsssssssss#",
"################",
"................",
"................",
"................",
"................"]

_logo_pixmap = QtGui.QPixmap(_logo_16x16_xpm)
