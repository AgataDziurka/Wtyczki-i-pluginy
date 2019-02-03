#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui, QtCore

class MinusIndicatorWidget(QtGui.QWidget):

    def __init__(self, parent=None):

        super(MinusIndicatorWidget, self).__init__(parent)

        self._color = QtGui.QColor("blue")
        self._maxhigh = 0
        self._minhigh = -100
        self._text = ' '
        self._position = 0
        self._value = 0

        self.setWindowTitle(QtCore.QObject.tr(self, "MinusIndicatorWidget"))
        self.resize(200, 100)

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
            self._position = self.width() - 10
        else:
            self._position = self.width() - 10 -  ((self.width() - 20)*((self._value * 100)/self._minhigh)/100)

        painter.drawRect(self._position, 10, 2, self.height()-20)

        painter.setPen(QtGui.QColor(168, 34, 3))
        painter.setFont(QtGui.QFont('Decorative', 10))
        painter.drawText(10, 10, self._text)
  
        painter.end()


    def minimumSizeHint(self):
        return QtCore.QSize(95, 60)

    def sizeHint(self):
        return QtCore.QSize(200, 95)

    def getMinhigh(self):
        return self._minhigh

    @QtCore.pyqtSlot(int)
    def setMinhigh(self, value):
        self._minhigh = value
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
    minhigh = QtCore.pyqtProperty(int, getMinhigh, setMinhigh)

if __name__ == "__main__":

    import sys

    app = QtGui.QApplication(sys.argv)
    wskaz = MinusIndicatorWidget()
    wskaz.show()
    sys.exit(app.exec_())
