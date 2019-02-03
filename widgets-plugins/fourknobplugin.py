#!/usr/bin/python
# -*- coding: utf-8 -*-


from PyQt4 import QtCore, QtGui
from PyQt4.QtDesigner import QPyDesignerCustomWidgetPlugin

from fourknobwidget import FourKnobWidget

class FourKnobPlugin(QPyDesignerCustomWidgetPlugin):

    def __init__(self, parent=None):
        super(FourKnobPlugin, self).__init__(parent)

        self.initialized = False

    def initialize(self, core):
        if self.initialized:
            return

        self.initialized = True

    def isInitialized(self):
        return self.initialized

    def createWidget(self, parent):
        return FourKnobWidget(parent)

    def name(self):
        return "FourKnobWidget"

    def toolTip(self):
        return ""

    def whatsThis(self):
        return ""

    def isContainer(self):
        return False

    def includeFile(self):
        return "fourknobwidget"

    def group(self):
        return "Control and measurement"

    def icon(self):
        return QtGui.QIcon(_logo_pixmap)

_logo_16x16_xpm = [
"16 16 4 1",
"z c #7ee46e",
"s c #464646",
"# c #000000",
". c #ffffff",
".....######.....",
"...#zzzzzzzz#...",
"..#zzzzzzzzzz#..",
".#zzzzz#zzzzzz#.",
".#zzzz#zzzzzzz#.",
"#zzzz#zzzzzzzzz#",
"#zzz#zzzzzzzzzz#",
"#zz####zsssssss#",
"#zzzzz#zsssssss#",
"#zzzzz#zzzzzzzz#",
"#zzzzz#nzzzzzzz#",
".#zzzz#zzzzzzz#.",
".#zzzzzzzzzzzz#.",
"..#zzzzzzzzzz#..",
"...#zzzzzzzz#...",
".....######....."]

_logo_pixmap = QtGui.QPixmap(_logo_16x16_xpm)    
