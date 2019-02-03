#!/usr/bin/python
# -*- coding: utf-8 -*-


from PyQt4 import QtCore, QtGui
from PyQt4.QtDesigner import QPyDesignerCustomWidgetPlugin

from threeknobwidget import ThreeKnobWidget

class ThreeKnobPlugin(QPyDesignerCustomWidgetPlugin):

    def __init__(self, parent=None):
        super(ThreeKnobPlugin, self).__init__(parent)

        self.initialized = False

    def initialize(self, core):
        if self.initialized:
            return

        self.initialized = True

    def isInitialized(self):
        return self.initialized

    def createWidget(self, parent):
        return ThreeKnobWidget(parent)

    def name(self):
        return "ThreeKnobWidget"

    def toolTip(self):
        return ""

    def whatsThis(self):
        return ""

    def isContainer(self):
        return False

    def includeFile(self):
        return "threeknobwidget"

    def group(self):
        return "Control and measurement"

    def icon(self):
        return QtGui.QIcon(_logo_pixmap)

_logo_16x16_xpm = [
"16 16 4 1",
"n c #7bd5f0",
"s c #464646",
"# c #000000",
". c #ffffff",
".....######.....",
"...#nnnnnnnn#...",
"..#nnnnnnnnnn#..",
".#n#####nnnnnn#.",
".#n#nnnn#nnnnn#.",
"#nnnnnn#nnnnnnn#",
"#nnnnn#nnnnnnnn#",
"#nnnn##nsssssss#",
"#nnnnn#nsssssss#",
"#nnnnnn#nnnnnnn#",
"#nn#nnnn#nnnnnn#",
".#nn####nnnnnn#.",
".#nnnnnnnnnnnn#.",
"..#nnnnnnnnnn#..",
"...#nnnnnnnn#...",
".....######....."]

_logo_pixmap = QtGui.QPixmap(_logo_16x16_xpm)    
