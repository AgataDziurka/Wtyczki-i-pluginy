#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui, QtCore

class TwoKnobWidget(QtGui.QWidget):

    moved = QtCore.pyqtSignal(int)
    onoff = QtCore.pyqtSignal(bool)

    def __init__(self, parent=None):

        super(TwoKnobWidget, self).__init__(parent)

        self.setWindowTitle(QtCore.QObject.tr(self, "TwoKnobWidget"))
        self.resize(200, 200)

        self._linecolor = QtGui.QColor(0, 0, 0)

        self._colorOUT = QtGui.QColor("black")
        self._colorOUTi = QtGui.QColor(252, 216, 90)
        self._colorIN = QtGui.QColor("black")
        self._colorINi = QtGui.QColor(137, 137, 137)

        self._numberPOS = 0
        self._state = False

        self._count = 0

    def paintEvent(self, event):

        side = min(self.width(), self.height())

        gradient = QtGui.QRadialGradient(0, 0, 80, 55, 9)
        gradient.setColorAt(1, self._colorOUT)
        gradient.setColorAt(0, self._colorOUTi)

        painter = QtGui.QPainter()
        painter.begin(self)

        brush = QtGui.QBrush(gradient)
        painter.setPen(self._colorOUT)

        painter.setRenderHint(QtGui.QPainter.Antialiasing, True)
        painter.translate(self.width() / 2, self.height() / 2)
        painter.scale(side / 200.0, side / 200.0)

        painter.setBrush(brush)

        painter.drawEllipse(-70, -70, 140, 140)

        painter.setPen(self._colorIN)
        gradient.setColorAt(1, self._colorIN)
        gradient.setColorAt(0, self._colorINi)
        brush = QtGui.QBrush(gradient)
        painter.setBrush(brush)

        if self._count == 0:
            painter.drawRect(0, -10, 70, 20)
        elif self._count == 1:
            painter.rotate(90)
            painter.drawRect(0, -10, 70, 20)

        painter.setPen(QtGui.QPen(self._linecolor))

        for j in range(0, 2):
            painter.drawLine(92, 0, 96, 0)

            if self._count == 0:
                painter.rotate(90)
            elif self._count == 1:
                painter.rotate(-90)

        painter.end()

    def mousePressEvent(self, event):

        if self._count == 0:
            self._numberPOS = 1
            self._state = True
            self._count += 1
        else:
            self._numberPOS = 0
            self._state = False
            self._count -= 1

        self.moved.emit(self._numberPOS)
        self.onoff.emit(self._state)
        
        self.update()

    def minimumSizeHint(self):

        return QtCore.QSize(50, 50)

    def sizeHint(self):

        return QtCore.QSize(100, 100)

    def getColor(self):
        return self._colorOUTi

    @QtCore.pyqtSlot(QtGui.QColor)
    def setColor(self, value):
        self._colorOUTi = value
        self.update()

    color = QtCore.pyqtProperty(QtGui.QColor, getColor, setColor)

if __name__ == "__main__":

    import sys
    app = QtGui.QApplication(sys.argv)
    knob = TwoKnobWidget()
    knob.show()
    sys.exit(app.exec_())
