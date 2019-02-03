#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui, QtCore

class HundredKnobWidget(QtGui.QWidget):

    moved = QtCore.pyqtSignal(int)

    def __init__(self, parent=None):

        super(HundredKnobWidget, self).__init__(parent)

        self.setWindowTitle(QtCore.QObject.tr(self, "HundredKnobWidget"))
        self.resize(200, 200)

        self._linecolor = QtGui.QColor(0, 0, 0)

        self._colorOUT = QtGui.QColor("black")
        self._colorOUTi = QtGui.QColor(228, 141, 110)
        self._colorIN = QtGui.QColor("black")
        self._colorINi = QtGui.QColor(137, 137, 137)

        self._dict= {1:3.6, 2:7.2, 3:10.8, 4:14.4, 5:18, 6:21.6,
                     7:25.2, 8:28.8, 9:32.4, 10:36, 11:39.6, 12:43.2,
                     13:46.8, 14:50.4, 15:54, 16:57.6, 17:61.2, 18:64.8,
                     19:68.4, 20:72, 21:75.6, 22:79.2, 23:82.8, 24:86.4,
                     25:90, 26:93.9, 27:97.2, 28:100.8, 29:104.4, 30:108,
                     31:111.6, 32:115.2, 33:118.8, 34:122.4, 35:126, 36:129.6,
                     37:133.2, 38:136.8, 39:140.4, 40:144, 41:147.6, 42:151.2,
                     43:154.8, 44:158.4, 45:162, 46:165.6, 47:169.2, 48:172.8,
                     49:176.4, 50:180, 51:183.6, 52:187.2, 53:190.8, 54:194.4,
                     55:198, 56:201.6, 57:205.2, 58:208.8, 59:212.4, 60:216,
                     61:219.6, 62:223.2, 63:226.8, 64:230.4, 65:234, 66:237.6,
                     67:241.2, 68:244.8, 69:248.4, 70:252, 71:255.6, 72:259.2,
                     73:262.8, 74:266.4, 75:270, 76:273.6, 77:277.2, 78:280.8,
                     79:284.4, 80:288, 81:291.6, 82:295.2, 83:298.8, 84:302.4,
                     85:306, 86:309.6, 87:313.2, 88:316.8, 89:320.4, 90:324,
                     91:327.6, 92:331.2, 93:334.8, 94:338.4, 95:342, 96:345.6,
                     97:349.2, 98:352.8, 99:356.4}

        self._table = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,
                       15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26,
                       27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38,
                       39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
                       51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62,
                       63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74,
                       75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86,
                       87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]

        self._numberPOS = 0

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

        painter.setPen(QtGui.QPen(self._linecolor))

        for j in range(0, 100):
            painter.drawLine(92, 0, 96, 0)
            painter.rotate(3.6)

        if self._count == 0:
            painter.drawRect(0, -10, 70, 5)
        elif self._count in self._dict.keys():
            painter.rotate(self._dict[self._count])
            painter.drawRect(0, -10, 70, 5)

        painter.end()

    def mousePressEvent(self, event):

        if self._count < 99:
            self._numberPOS = self._table[self._count]
            self._count += 1
        else:
            self._numberPOS = 0
            self._count = 0

        self.moved.emit(self._numberPOS)
        
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
    knob = HundredKnobWidget()
    knob.show()
    sys.exit(app.exec_())
