import sys
import solver
from board import Board
from PyQt5 import QtGui,QtCore
from PyQt5.QtWidgets import QApplication,QWidget,QTableWidgetItem
from sudoku_ui import Ui_Form

class SudokuWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.PB_gen_puzzle.clicked.connect(self.gen_puzzle)
        self.ui.PB_solve_puzzle.clicked.connect(self.solve_puzzle)

        table = self.ui.tableWidget
        for i in range(9):
            for j in range(9):
                table.setItem(i,j,QTableWidgetItem())

        pallet = QtGui.QPalette()
        pallet.setColor(QtGui.QPalette.Text, QtCore.Qt.red)
        table.setFont(QtGui.QFont('Helvetica',44,QtGui.QFont.Bold))

        

    def gen_puzzle(self):
        print("gen puzzle")
        b1 = Board()
        solver.generate_puzzle(b1.bd)
#        b1.display(stop=True)

        table = self.ui.tableWidget
        for i in range(9):
            for j in range(9):
                if b1.bd[i][j]:
#                    print(f'({i},{j}) = {b1.bd[i][j]}')
                    table.item(i,j).setText(str(b1.bd[i][j]))
                    table.item(i,j).setTextAlignment(QtCore.Qt.AlignCenter)
                    table.item(i,j).setForeground(QtCore.Qt.green)
        table.viewport().update()



    def solve_puzzle(self):
        print("solve puzzle")
