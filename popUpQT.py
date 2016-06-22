import sys
from PyQt4 import QtGui, QtCore
from labs_dict import labs
from OpenFolders import LeveyJennings

class MyWindow(QtGui.QWidget):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setGeometry(50, 50, 300, 200)
        self.setWindowTitle('Select an Option')
        self.setWindowIcon(QtGui.QIcon('D:\Images\Logos\CLMS Logo_cropped.png'))
        self.data_btn = QtGui.QPushButton('Data')
        self.graph_btn = QtGui.QPushButton('Graphs')
        self.data_btn.clicked.connect(self.pop_up_data_window)
        layout = QtGui.QHBoxLayout()
        layout.addWidget(self.data_btn)
        layout.addWidget(self.graph_btn)
        self.setLayout(layout)
        self.show()

    def pop_up_data_window(self):
        child = DataWindow(self)
        child.show()


class DataWindow(QtGui.QDialog):
    def __init__(self, parent=None):
        super(DataWindow, self).__init__(parent)
        self.setGeometry(55, 55, 300, 200)
        self.setWindowTitle('Select a Lab')
        self.setWindowIcon(QtGui.QIcon('D:\Images\Logos\CLMS Logo_cropped.png'))

        # list of lab names from dictionary
        self.labs = list(sorted(labs.keys()))
        self.combo_box = QtGui.QComboBox()
        layout = QtGui.QHBoxLayout()

        # add all dict keys to drop down
        for x in range(len(self.labs)):
            self.combo_box.addItem(self.labs[x])
        layout.addWidget(self.combo_box)

        layout.addStretch(1)
        self.submit_btn = QtGui.QPushButton('Submit')
        self.submit_btn.resize(50,50)
        layout.addWidget(self.submit_btn)
        self.setLayout(layout)
        self.submit_btn.clicked.connect(self.submit_labs)
        self.show()

    def submit_labs(self):
        lab_selected = self.combo_box.currentText()
        lab_value = labs.get(lab_selected, None)
        pop_up = Loading_Dialogue(self)
        levey = LeveyJennings(lab_value)
        levey.results_folder()
        pop_up.show()
        pop_up.close()
        self.close()


class Loading_Dialogue(QtGui.QDialog):
    def __init__(self, parent=None):
        super(Loading_Dialogue, self).__init__(parent)
        self.setGeometry(80, 80, 200, 50)
        self.setWindowTitle('Status')
        self.setWindowIcon(QtGui.QIcon('D:\Images\Logos\CLMS Logo_cropped.png'))
        self.text = QtGui.QLabel("Data is processing...", self)
        layout = QtGui.QHBoxLayout()
        layout.addWidget(self.text)
        self.setLayout(layout)
        self.show()

if __name__ == '__main__':
    app = QtGui.QApplication([])
    window = MyWindow()
    window.show()
    app.exec_()