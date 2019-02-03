#!/usr/bin/python
# -*- coding: utf-8 -*-


from PyQt4 import QtCore, QtGui
from PyQt4.QtDesigner import QPyDesignerCustomWidgetPlugin

from upindicatorwidget import UpIndicatorWidget

class UpIndicatorPlugin(QPyDesignerCustomWidgetPlugin):

    def __init__(self, parent=None):
        super(UpIndicatorPlugin, self).__init__(parent)

        self.initialized = False

    def initialize(self, core):
        if self.initialized:
            return

        self.initialized = True

    def isInitialized(self):
        return self.initialized

    def createWidget(self, parent):
        return UpIndicatorWidget(parent)

    def name(self):
        return "UpIndicatorWidget"

    def toolTip(self):
        return ""

    def whatsThis(self):
        return ""

    def isContainer(self):
        return False

    def includeFile(self):
        return "upindicatorwidget"

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
"....########....",
"....#ssssss#....",
"....#ssssss#....",
"....#ssssss#....",
"....#ssssss#....",
"....#ssssss#....",
"....#ssssss#....",
"....#pppppp#....",
"....#pppppp#....",
"....#ssssss#....",
"....#ssssss#....",
"....#ssssss#....",
"....#ssssss#....",
"....########....",
"................"]

_logo_pixmap = QtGui.QPixmap(_logo_16x16_xpm)
