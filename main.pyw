# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\levey_main_dialog.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

import os
from PyQt4 import QtCore, QtGui
from data_main import generate_data
from data_main import get_home
from graph_package import make_graph
from graph_package import validate_data_csv
import loading_dialog
import warning_popup
from labs_dict import get_labs
import tkinter
from tkinter import filedialog

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


class Ui_graph_tab(object):
    def setupUi(self, graph_tab):
        graph_tab.setObjectName(_fromUtf8("graph_tab"))
        graph_tab.resize(344, 192)
        self.generate_data_tab = QtGui.QWidget()
        self.generate_data_tab.setObjectName(_fromUtf8("generate_data_tab"))
        self.horizontalLayoutWidget = QtGui.QWidget(self.generate_data_tab)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(250, 30, 81, 80))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.submit_labs_data = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.submit_labs_data.setObjectName(_fromUtf8("submit_labs_data"))
        self.submit_labs_data.clicked.connect(self.submit_labs)
        self.horizontalLayout.addWidget(self.submit_labs_data)
        self.verticalLayoutWidget_2 = QtGui.QWidget(self.generate_data_tab)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(39, 30, 201, 80))
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))

        # Add lab names to combo box
        self.lab_combo_box = QtGui.QComboBox(self.verticalLayoutWidget_2)
        self.lab_combo_box.setObjectName(_fromUtf8("lab_combo_box"))
        self.labs_list = list(sorted(get_labs().keys()))
        for x in range(len(self.labs_list)):
            self.lab_combo_box.addItem(self.labs_list[x])

        self.verticalLayout.addWidget(self.lab_combo_box)
        self.horizontalLayoutWidget_2 = QtGui.QWidget(self.generate_data_tab)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(39, 30, 201, 31))
        self.horizontalLayoutWidget_2.setObjectName(_fromUtf8("horizontalLayoutWidget_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label = QtGui.QLabel(self.horizontalLayoutWidget_2)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        graph_tab.addTab(self.generate_data_tab, _fromUtf8(""))
        self.graph_data_tab = QtGui.QWidget()
        self.graph_data_tab.setObjectName(_fromUtf8("graph_data_tab"))
        self.horizontalLayoutWidget_4 = QtGui.QWidget(self.graph_data_tab)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(250, 50, 81, 80))
        self.horizontalLayoutWidget_4.setObjectName(_fromUtf8("horizontalLayoutWidget_4"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))

        self.submit_file_button = QtGui.QPushButton(self.horizontalLayoutWidget_4)
        self.submit_file_button.setObjectName(_fromUtf8("submit_file_button"))
        self.submit_file_button.clicked.connect(self.create_graphs)

        self.horizontalLayout_4.addWidget(self.submit_file_button)
        self.verticalLayoutWidget = QtGui.QWidget(self.graph_data_tab)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(40, 19, 201, 111))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_2 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_2.setLineWidth(0)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_3.addWidget(self.label_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.select_file_button = QtGui.QPushButton(self.verticalLayoutWidget)
        self.select_file_button.setObjectName(_fromUtf8("select_file_button"))
        self.verticalLayout_2.addWidget(self.select_file_button)
        self.select_file_button.clicked.connect(self.file_pop_up)

        self.display_file_name = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.display_file_name.setObjectName(_fromUtf8("display_file_name"))
        self.verticalLayout_2.addWidget(self.display_file_name)
        graph_tab.addTab(self.graph_data_tab, _fromUtf8(""))

        self.retranslateUi(graph_tab)
        graph_tab.setCurrentIndex(1)
        # QtCore.QObject.connect(self.select_file_button, QtCore.SIGNAL(_fromUtf8("clicked()")),
        # self.display_file_name.paste)
        QtCore.QMetaObject.connectSlotsByName(graph_tab)

    def retranslateUi(self, graph_tab):
        graph_tab.setWindowTitle(_translate("graph_tab", "Select an Option", None))
        self.submit_labs_data.setText(_translate("graph_tab", "Submit", None))
        self.label.setText(_translate("graph_tab", "Please select a lab:", None))
        graph_tab.setTabText(graph_tab.indexOf(self.generate_data_tab), _translate("graph_tab", "Generate Data", None))
        self.submit_file_button.setText(_translate("graph_tab", "Submit", None))
        self.label_2.setText(_translate("graph_tab", "Select the data.csv file to graph:", None))
        self.select_file_button.setText(_translate("graph_tab", "Select File", None))
        graph_tab.setTabText(graph_tab.indexOf(self.graph_data_tab), _translate("graph_tab", "Graph Data", None))

    def submit_labs(self, generate_data_tab):
        lab_selected = self.lab_combo_box.currentText()
        lab_value = get_labs()[lab_selected]
        self.create_data(lab_value)

    def create_data(self, lab_value):
        loading = QtGui.QDialog()
        ui_load = loading_dialog.Ui_Loading()
        ui_load.setupUi(loading)
        loading.show()
        loading.repaint()
        generate_data(lab_value)
        loading.close()

    def file_pop_up(self):
        home = get_home()
        results_directory = os.path.join(home, 'Results')
        self.display_file_name.setText(QtGui.QFileDialog.getOpenFileName(None, None, results_directory))

    def create_graphs(self):
        file_name = self.display_file_name.text()
        data_validity = validate_data_csv(file_name)
        if data_validity:
            month_directory = os.path.dirname(file_name)
            lab_directory = os.path.dirname(month_directory)
            lab_name = os.path.basename(lab_directory)
            loading = QtGui.QDialog()
            ui_load = loading_dialog.Ui_Loading()
            ui_load.setupUi(loading)
            loading.show()
            loading.repaint()
            make_graph(lab_name, file_name)
            loading.close()
        else:
            warning = QtGui.QDialog()
            ui = warning_popup.Ui_warning_dialog()
            ui.setupUi(warning)
            warning.show()
            warning.exec_()
            # warning.repaint()
            return

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon('CLMS_Logo_cropped.png'))
    graph_tab = QtGui.QTabWidget()
    ui = Ui_graph_tab()
    ui.setupUi(graph_tab)
    graph_tab.show()
    sys.exit(app.exec_())

