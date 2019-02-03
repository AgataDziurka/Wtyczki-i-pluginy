#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
from PyQt4.QtDesigner import QPyDesignerCustomWidgetPlugin

from ledwidget import LedWidget

class LedPlugin(QPyDesignerCustomWidgetPlugin):

    def __init__(self, parent=None):
        super(LedPlugin, self).__init__(parent)

        self.initialized = False

    def initialize(self, core):
        if self.initialized:
            return

        self.initialized = True

    def isInitialized(self):
        return self.initialized

    def createWidget(self, parent):
        return LedWidget(parent)

    def name(self):
        return "LedWidget"

    def toolTip(self):
        return ""

    def whatsThis(self):
        return ""

    def isContainer(self):
        return False

    def includeFile(self):
        return "ledwidget"
    
    def group(self):
        return "Control and measurement"

    def icon(self):
        return QtGui.QIcon(_logo_pixmap)

_logo_16x16_xpm = [
"16 16 3 1",
"c c #e80000",
"# c #000000",
". c #ffffff",
".....######.....",
"...#cccccccc#...",
"..#c..ccccccc#..",
".#c...cccccccc#.",
".#c..ccccccccc#.",
"#cc.ccccccccccc#",
"#cccccccccccccc#",
"#cccccccccccccc#",
"#cccccccccccccc#",
"#cccccccccccccc#",
"#cccccccccccccc#",
".#cccccccccccc#.",
".#cccccccccccc#.",
"..#cccccccccc#..",
"...#cccccccc#...",
".....######....."]

_logo_pixmap = QtGui.QPixmap(_logo_16x16_xpm)    
