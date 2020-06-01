# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sudoku.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(764, 566)
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(20, 30, 431, 431))
        self.tableWidget.setAutoScroll(False)
        self.tableWidget.setAlternatingRowColors(False)
        self.tableWidget.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.tableWidget.setRowCount(9)
        self.tableWidget.setColumnCount(9)
        self.tableWidget.setObjectName("tableWidget")
        # item = QtWidgets.QTableWidgetItem()
        # item.setTextAlignment(QtCore.Qt.AlignCenter)
        # font = QtGui.QFont()
        # font.setPointSize(44)
        # font.setBold(True)
        # font.setWeight(75)
        # item.setFont(font)
        # brush = QtGui.QBrush(QtGui.QColor(220, 220, 220))
        # brush.setStyle(QtCore.Qt.NoBrush)
        # item.setBackground(brush)
        # item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        # self.tableWidget.setItem(0, 0, item)
        # item = QtWidgets.QTableWidgetItem()
        # brush = QtGui.QBrush(QtGui.QColor(197, 197, 197))
        # brush.setStyle(QtCore.Qt.NoBrush)
        # item.setBackground(brush)
        # self.tableWidget.setItem(0, 1, item)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(48)
        self.tableWidget.horizontalHeader().setHighlightSections(False)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(48)
        self.tableWidget.verticalHeader().setHighlightSections(False)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(510, 30, 221, 431))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.PB_gen_puzzle = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.PB_gen_puzzle.setObjectName("PB_gen_puzzle")
        self.verticalLayout.addWidget(self.PB_gen_puzzle)
        self.PB_solve_puzzle = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.PB_solve_puzzle.setObjectName("PB_solve_puzzle")
        self.verticalLayout.addWidget(self.PB_solve_puzzle)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.PB_exit = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.PB_exit.setObjectName("PB_exit")
        self.verticalLayout.addWidget(self.PB_exit)
        self.PB_reset_table = QtWidgets.QPushButton(Form)
        self.PB_reset_table.setGeometry(QtCore.QRect(200, 490, 113, 41))
        self.PB_reset_table.setObjectName("PB_reset_table")

        self.retranslateUi(Form)
        self.PB_exit.clicked.connect(Form.close)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.PB_gen_puzzle.setText(_translate("Form", "Generate Puzzle"))
        self.PB_solve_puzzle.setText(_translate("Form", "Solve Puzzle"))
        self.PB_exit.setText(_translate("Form", "Exit"))
        self.PB_reset_table.setText(_translate("Form", "Reset"))

