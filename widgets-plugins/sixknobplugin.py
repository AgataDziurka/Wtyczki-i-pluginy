#!/usr/bin/python
# -*- coding: utf-8 -*-


from PyQt4 import QtCore, QtGui
from PyQt4.QtDesigner import QPyDesignerCustomWidgetPlugin

from sixknobwidget import SixKnobWidget

class SixKnobPlugin(QPyDesignerCustomWidgetPlugin):

    def __init__(self, parent=None):
        super(SixKnobPlugin, self).__init__(parent)

        self.initialized = False

    def initialize(self, core):
        if self.initialized:
            return

        self.initialized = True

    def isInitialized(self):
        return self.initialized

    def createWidget(self, parent):
        return SixKnobWidget(parent)

    def name(self):
        return "SixKnobWidget"

    def toolTip(self):
        return ""

    def whatsThis(self):
        return ""

    def isContainer(self):
        return False

    def includeFile(self):
        return "sixknobwidget"

    def group(self):
        return "Control and measurement"

    def icon(self):
        return QtGui.QIcon(_logo_pixmap)

_logo_16x16_xpm = [
"16 16 4 1",
"f c #b56ee4",
"s c #464646",
"# c #000000",
". c #ffffff",
".....######.....",
"...#ffffffff#...",
"..#ffffffffff#..",
".#ff###fffffff#.",
".#f#fff#ffffff#.",
"#f#ffffffffffff#",
"#f#ffffffffffff#",
"#f#####fsssssss#",
"#f#ffff#sssssss#",
"#f#ffff#fffffff#",
"#ff#ff#ffffffff#",
".#ff##ffffffff#.",
".#ffffffffffff#.",
"..#ffffffffff#..",
"...#ffffffff#...",
".....######....."]

_logo_pixmap = QtGui.QPixmap(_logo_16x16_xpm)    
