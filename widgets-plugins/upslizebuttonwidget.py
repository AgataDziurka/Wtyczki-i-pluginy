#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui, QtCore

class UpslizebuttonWidget(QtGui.QWidget):

    punched = QtCore.pyqtSignal(bool)
    
    def __init__(self, parent=None):

        super(UpslizebuttonWidget, self).__init__(parent)
        
        self._colorON = QtGui.QColor("green")
        self._colorONi = QtGui.QColor(131, 183, 123)
        self._colorOFF = QtGui.QColor("red")
        self._colorOFFi = QtGui.QColor(223, 117, 117)
        self._colorSLIDE = QtGui.QColor("black")
        self._colorSLIDEi = QtGui.QColor(105, 105, 105)
        
        self._stateGive = True

        self._positionY = 0

        self.setWindowTitle(QtCore.QObject.tr(self, "UpslizebuttonWidget"))
        self.resize(50, 200)

    def paintEvent(self, event):

        painter = QtGui.QPainter()

        half = self.height()/2

        painter.begin(self)
        painter.setPen(self._colorOFF)
        painter.setBrush(self._colorOFFi)
        painter.setRenderHint(QtGui.QPainter.Antialiasing, True)

        painter.drawRect(0, half, self.width(), self.height()/2)
        
        painter.setPen(self._colorON)
        painter.setBrush(self._colorONi)

        painter.drawRect(0, 0, self.width(), self.height()/2)
        
        painter.setPen(self._colorSLIDE)
        painter.setBrush(self._colorSLIDEi)

        painter.drawRect(0, self._positionY, self.width(), half)

        painter.end()

    def mousePressEvent(self, event):

        if event.button() == QtCore.Qt.LeftButton:
            
            if self._positionY == 0:
                self._positionY= self.height()/2
                self._stateGive = True
            elif self._positionY == self.height()/2:
                self._positionY = 0
                self._stateGive = False
                
        self.punched.emit(self._stateGive)
        self.update()

    def minimumSizeHint(self):

        return QtCore.QSize(13, 25)

    def sizeHint(self):

        return QtCore.QSize(25, 50)

if __name__ == "__main__":

    import sys
    app = QtGui.QApplication(sys.argv)
    ubutton = UpslizebuttonWidget()
    ubutton.show()
    sys.exit(app.exec_())
