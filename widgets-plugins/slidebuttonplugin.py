#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
from PyQt4.QtDesigner import QPyDesignerCustomWidgetPlugin

from slidebuttonwidget import SlidebuttonWidget

class SlideButtonPlugin(QPyDesignerCustomWidgetPlugin):

    def __init__(self, parent=None):
        super(SlideButtonPlugin, self).__init__(parent)

        self.initialized = False

    def initialize(self, core):
        if self.initialized:
            return

        self.initialized = True

    def isInitialized(self):
        return self.initialized

    def createWidget(self, parent):
        return SlidebuttonWidget(parent)

    def name(self):
        return "SlidebuttonWidget"

    def toolTip(self):
        return ""

    def whatsThis(self):
        return ""

    def isContainer(self):
        return False

    def includeFile(self):
        return "slidebuttonwidget"
    
    def group(self):
        return "Control and measurement"

    def icon(self):
        return QtGui.QIcon(_logo_pixmap)

_logo_16x16_xpm = [
"16 16 4 1",
"z c #63b640",
"s c #9a9a9a",
"# c #000000",
". c #ffffff",
"................",
"................",
"................",
"................",
"################",
"#zzzzzz##ssssss#",
"#zzzzzz##ssssss#",
"#zzzzzz##ssssss#",
"#zzzzzz##ssssss#",
"#zzzzzz##ssssss#",
"#zzzzzz##ssssss#",
"################",
"................",
"................",
"................",
"................"]

_logo_pixmap = QtGui.QPixmap(_logo_16x16_xpm) 
