# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\loading_dialog.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_Loading(object):
    def setupUi(self, Loading):
        Loading.setObjectName(_fromUtf8("Loading"))
        Loading.resize(344, 101)
        self.label = QtGui.QLabel(Loading)
        self.label.setGeometry(QtCore.QRect(80, 40, 161, 20))
        self.label.setAutoFillBackground(True)
        self.label.setLineWidth(0)
        self.label.setObjectName(_fromUtf8("label"))
        self.retranslateUi(Loading)
        QtCore.QMetaObject.connectSlotsByName(Loading)

    def retranslateUi(self, Loading):
        Loading.setWindowTitle(_translate("Loading", "Loading...", None))
        self.label.setText(_translate("Loading", "Data is processing...Please wait", None))


def main():
    app = QtGui.QApplication(sys.argv)
    Loading = QtGui.QDialog()
    ui = Ui_Loading()
    ui.setupUi(Loading)
    Loading.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
