#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui, QtCore

class LedWidget(QtGui.QWidget):
    
    def __init__(self, parent=None):

        super(LedWidget, self).__init__(parent)

        self._color = QtGui.QColor("red")
        self._bazecolor = self._color
        self._color1 = QtGui.QColor("blue")
        self._color2 = QtGui.QColor("green")
        self._state = False

        self.setWindowTitle(QtCore.QObject.tr(self, "LedWidget"))
        self.resize(200, 200)

    def paintEvent(self, event):
        
        painter = QtGui.QPainter()

        side = min(self.width(), self.height())

        gradient = QtGui.QRadialGradient(self.width()/3, self.height()/3,
                                   side/4, side/4, side/2)
        gradient.setColorAt(0, QtGui.QColor(255, 255, 255))

        if self._state == True:
            gradient.setColorAt(1, self._color)
        else:
            gradient.setColorAt(1, QtGui.QColor(0, 0, 0))

        painter.begin(self)
        brush = QtGui.QBrush(gradient)
        painter.setPen(self._color)
        painter.setRenderHint(QtGui.QPainter.Antialiasing, True)
        painter.setBrush(brush)

        painter.drawEllipse(self.width()/4, self.height()/4, side/2, side/2)

        painter.end()

    def minimumSizeHint(self):

        return QtCore.QSize(25, 25)

    def sizeHint(self):

        return QtCore.QSize(50, 50)

    def getColor(self):
        return self._color

    @QtCore.pyqtSlot(QtGui.QColor)
    def setColor(self, value):
        self._color = value
        self._bazecolor = self._color
        self.update()

    def getColor1(self):
        return self._color1

    @QtCore.pyqtSlot(QtGui.QColor)
    def setColor1(self, value):
        self._color1 = value
        self.update()

    def getColor2(self):
        return self._color2

    @QtCore.pyqtSlot(QtGui.QColor)
    def setColor2(self, value):
        self._color2 = value
        self.update()

    @QtCore.pyqtSlot(int)
    def changeColor(self, value):
        if value == 0:
            self._color = self._bazecolor
        elif value == 1:
            self._color = self._color1
        elif value == 2:
            self._color = self._color2
        self.update()

    def getState(self):
        return self._state

    @QtCore.pyqtSlot(bool)
    def setState(self, value):
        self._state = value
        self.update()

    color = QtCore.pyqtProperty(QtGui.QColor, getColor, setColor)
    color1 = QtCore.pyqtProperty(QtGui.QColor, getColor1, setColor1)
    color2 = QtCore.pyqtProperty(QtGui.QColor, getColor2, setColor2)
    state = QtCore.pyqtProperty(bool, getState, setState)

if __name__ == "__main__":

    import sys

    app = QtGui.QApplication(sys.argv)
    led = LedWidget()
    led.show()
    sys.exit(app.exec_())
