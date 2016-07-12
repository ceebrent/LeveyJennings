from PyQt4 import QtGui, QtCore
import sys
from labs_dict import labs
from data_main import generate_data


class Window(QtGui.QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50, 50, 300, 200)
        self.setWindowTitle('Select an Option')
        self.setWindowIcon(QtGui.QIcon('D:\Images\Logos\CLMS Logo_cropped.png'))
        self.home()

    def home(self):
        data_btn = QtGui.QPushButton('Data', self)
        graph_btn = QtGui.QPushButton('Graphs', self)
        data_btn.clicked.connect(self.data_pop_up)
        layout = QtGui.QHBoxLayout()
        layout.addWidget(data_btn)
        layout.addWidget(graph_btn)
        self.setLayout(layout)
        self.show()

    def data_pop_up(self):
        data_window = QtGui.QDialog(self)
        data_window.setWindowTitle('Select a Lab')
        data_window.setWindowIcon(QtGui.QIcon('D:\Images\Logos\CLMS Logo_cropped.png'))
        layout = QtGui.QHBoxLayout()

        # list of lab names from dictionary
        labs_list = list(sorted(labs.keys()))
        self.combo_box = QtGui.QComboBox()

        # add all dict keys to drop down
        for x in range(len(labs_list)):
            self.combo_box.addItem(labs_list[x])
        layout.addWidget(self.combo_box)

        layout.addStretch(1)
        submit_btn = QtGui.QPushButton('Submit', self)
        submit_btn.resize(50, 50)
        layout.addWidget(submit_btn)
        submit_btn.clicked.connect(self.submit_labs)
        data_window.setLayout(layout)
        data_window.show()

    def submit_labs(self):
        lab_selected = self.combo_box.currentText()
        lab_value = labs.get(lab_selected, None)
        print(lab_value)
        self.close()


def run():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())


run()
