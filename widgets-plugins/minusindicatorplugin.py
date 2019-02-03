#!/usr/bin/python
# -*- coding: utf-8 -*-


from PyQt4 import QtCore, QtGui
from PyQt4.QtDesigner import QPyDesignerCustomWidgetPlugin

from minusindicatorwidget import MinusIndicatorWidget

class MinusIndicatorPlugin(QPyDesignerCustomWidgetPlugin):

    def __init__(self, parent=None):
        super(MinusIndicatorPlugin, self).__init__(parent)

        self.initialized = False

    def initialize(self, core):
        if self.initialized:
            return

        self.initialized = True

    def isInitialized(self):
        return self.initialized

    def createWidget(self, parent):
        return MinusIndicatorWidget(parent)

    def name(self):
        return "MinusIndicatorWidget"

    def toolTip(self):
        return ""

    def whatsThis(self):
        return ""

    def isContainer(self):
        return False

    def includeFile(self):
        return "minusindicatorwidget"

    def group(self):
        return "Control and measurement"

    def icon(self):
        return QtGui.QIcon(_logo_pixmap)

_logo_16x16_xpm = [
"16 16 4 1",
"b c #0022ff",
"s c #8e8e8e",
"# c #000000",
". c #ffffff",
"................",
"..############..",
"................",
"................",
"################",
"#sssssssssbbsss#",
"#sssssssssbbsss#",
"#sssssssssbbsss#",
"#sssssssssbbsss#",
"#sssssssssbbsss#",
"#sssssssssbbsss#",
"################",
"................",
"................",
"................",
"................"]

_logo_pixmap = QtGui.QPixmap(_logo_16x16_xpm)
