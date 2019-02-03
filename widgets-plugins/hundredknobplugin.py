#!/usr/bin/python
# -*- coding: utf-8 -*-


from PyQt4 import QtCore, QtGui
from PyQt4.QtDesigner import QPyDesignerCustomWidgetPlugin

from hundredknobwidget import HundredKnobWidget

class HundredKnobPlugin(QPyDesignerCustomWidgetPlugin):

    def __init__(self, parent=None):
        super(HundredKnobPlugin, self).__init__(parent)

        self.initialized = False

    def initialize(self, core):
        if self.initialized:
            return

        self.initialized = True

    def isInitialized(self):
        return self.initialized

    def createWidget(self, parent):
        return HundredKnobWidget(parent)

    def name(self):
        return "HundredKnobWidget"

    def toolTip(self):
        return ""

    def whatsThis(self):
        return ""

    def isContainer(self):
        return False

    def includeFile(self):
        return "hundredknobwidget"

    def group(self):
        return "Control and measurement"

    def icon(self):
        return QtGui.QIcon(_logo_pixmap)

_logo_16x16_xpm = [
"16 16 4 1",
"b c #e48d6e",
"s c #464646",
"# c #000000",
". c #ffffff",
".....######.....",
"...#bbbbbbbb#...",
"..#bbbbbbbbbb#..",
".#bbbbbbbbbbbb#.",
".#bbbbbbbbbbbb#.",
"#bbbbbbbbbbbbbb#",
"#bbbbbbbbbbbbbb#",
"#bbbbbbbsssssss#",
"#bbbbbbbsssssss#",
"#bbbbbbbbbbbbbb#",
"#bbbbbbbbbbbbbb#",
".#bbbbbbbbbbbb#.",
".#bbbbbbbbbbbb#.",
"..#bbbbbbbbbb#..",
"...#bbbbbbbb#...",
".....######....."]

_logo_pixmap = QtGui.QPixmap(_logo_16x16_xpm)    
