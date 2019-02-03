#!/usr/bin/python
# -*- coding: utf-8 -*-


from PyQt4 import QtCore, QtGui
from PyQt4.QtDesigner import QPyDesignerCustomWidgetPlugin

from twoknobwidget import TwoKnobWidget

class TwoKnobPlugin(QPyDesignerCustomWidgetPlugin):

    def __init__(self, parent=None):
        super(TwoKnobPlugin, self).__init__(parent)

        self.initialized = False

    def initialize(self, core):
        if self.initialized:
            return

        self.initialized = True

    def isInitialized(self):
        return self.initialized

    def createWidget(self, parent):
        return TwoKnobWidget(parent)

    def name(self):
        return "TwoKnobWidget"

    def toolTip(self):
        return ""

    def whatsThis(self):
        return ""

    def isContainer(self):
        return False

    def includeFile(self):
        return "twoknobwidget"

    def group(self):
        return "Control and measurement"

    def icon(self):
        return QtGui.QIcon(_logo_pixmap)

_logo_16x16_xpm = [
"16 16 4 1",
"z c #e9de3a",
"s c #464646",
"# c #000000",
". c #ffffff",
".....######.....",
"...#zzzzzzzz#...",
"..#zzzzzzzzzz#..",
".#z####zzzzzzz#.",
".#z#zzz#zzzzzz#.",
"#zzzzzz#zzzzzzz#",
"#zzzzzz#sssssss#",
"#zzzzz#zsssssss#",
"#zzzz#zzsssssss#",
"#zzz#zzzzzzzzzz#",
"#zz######zzzzzz#",
".#zzzzzzzzzzzz#.",
".#zzzzzzzzzzzz#.",
"..#zzzzzzzzzz#..",
"...#zzzzzzzz#...",
".....######....."]

_logo_pixmap = QtGui.QPixmap(_logo_16x16_xpm)    
