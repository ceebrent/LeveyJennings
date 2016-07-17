# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'warning_popup.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class Ui_warning_dialog(object):
    def setupUi(self, warning_dialog):
        warning_dialog.setObjectName(_fromUtf8("warning_dialog"))
        warning_dialog.resize(331, 54)
        self.warning_label = QtGui.QLabel(warning_dialog)
        self.warning_label.setGeometry(QtCore.QRect(80, 20, 171, 16))
        self.warning_label.setAutoFillBackground(False)
        self.warning_label.setLineWidth(0)
        self.warning_label.setObjectName(_fromUtf8("warning_label"))

        self.retranslateUi(warning_dialog)
        QtCore.QMetaObject.connectSlotsByName(warning_dialog)

    def retranslateUi(self, warning_dialog):
        warning_dialog.setWindowTitle(_translate("warning_dialog", "Warning - Incorrect File", None))
        self.warning_label.setText(_translate("warning_dialog", "Please select only a data.csv file", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    warning_dialog = QtGui.QDialog()
    ui = Ui_warning_dialog()
    ui.setupUi(warning_dialog)
    warning_dialog.show()
    sys.exit(app.exec_())

