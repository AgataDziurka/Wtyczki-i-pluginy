#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui, QtCore

class UpIndicatorWidget(QtGui.QWidget):

    def __init__(self, parent=None):

        super(UpIndicatorWidget, self).__init__(parent)

        self._color = QtGui.QColor("orange")
        self._maxhigh = 100
        self._minhigh = 0
        self._text = ' '
        self._position = 0
        self._value = 0

        self.setWindowTitle(QtCore.QObject.tr(self, "UpIndicatorWidget"))
        self.resize(100, 200)

    def paintEvent(self, event):

        painter = QtGui.QPainter()
        painter.begin(self)
        painter.setPen(QtGui.QColor(137, 137, 137))
        painter.setBrush(QtGui.QColor(155, 157, 137))
        painter.setRenderHint(QtGui.QPainter.Antialiasing, True)

        painter.drawRect(10, 10, self.width()-20, self.height()-20)
        
        painter.setPen(self._color)
        painter.setBrush(self._color)

        if self._value == 0:
            self._position = self.height() - 10
        else:
            self._position = self.height() - 10 - ((self.height() - 20)*((self._value * 100)/self._maxhigh)/100)

        painter.drawRect(10, self._position, self.width()-20, 2)

        painter.setPen(QtGui.QColor(168, 34, 3))
        painter.setFont(QtGui.QFont('Decorative', 10))
        painter.drawText(10, 10, self._text)
  
        painter.end()


    def minimumSizeHint(self):
        return QtCore.QSize(60, 95)

    def sizeHint(self):
        return QtCore.QSize(95, 200)

    def getMaxhigh(self):
        return self._maxhigh

    @QtCore.pyqtSlot(int)
    def setMaxhigh(self, value):
        self._maxhigh = value
        self.update()

    def getColor(self):
        return self._color

    @QtCore.pyqtSlot(QtGui.QColor)
    def setColor(self, value):
        self._color = value
        self.update()

    @QtCore.pyqtSlot(int)
    def updatePoint(self, value):
        if value > self._maxhigh:
            value = self._maxhigh
            self._text = 'Error: Too high'
        elif value < self._minhigh:
            value = self._minhigh
            self._text = 'Error: Too low'
        else:
            self._text = ' '
        self._value = value
        self.update()

    color = QtCore.pyqtProperty(QtGui.QColor, getColor, setColor)
    maxhigh = QtCore.pyqtProperty(int, getMaxhigh, setMaxhigh)

if __name__ == "__main__":

    import sys

    app = QtGui.QApplication(sys.argv)
    wskaz = UpIndicatorWidget()
    wskaz.show()
    sys.exit(app.exec_())
