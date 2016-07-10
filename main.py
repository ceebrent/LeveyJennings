from popUpQT import MyWindow
from PyQt4 import QtGui


if __name__ == '__main__':
    app = QtGui.QApplication([])
    window = MyWindow()
    window.show()
    app.exec_()