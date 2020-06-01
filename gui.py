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
        self.ui.PB_reset_table.clicked.connect(self.resetTable)

        table = self.ui.tableWidget
        for i in range(9):
            for j in range(9):
                item = QTableWidgetItem()
                if ((i//3 + j//3)%2):
#                    item.setBackground(QtCore.Qt.lightGray)
                    item.setBackground(QtGui.QColor(220,220,220,127))
                table.setItem(i,j,item)

        pallet = QtGui.QPalette()
        pallet.setColor(QtGui.QPalette.Text, QtCore.Qt.red)
        table.setFont(QtGui.QFont('Helvetica',44,QtGui.QFont.Bold))

        

    def gen_puzzle(self):
        print("gen puzzle")
        b1 = Board()
        solver.generate_puzzle(b1.bd)
#        b1.display(stop=True)

        self.resetTable()
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
        b1 = Board()
        table = self.ui.tableWidget
        data = []
        for i in range(9):
            s = ""
            for j in range(9):
                n = table.item(i,j).text()
                print(f'({i},{j}) = {n}')
                if not n : s += '0'
                else: s+= n
            data.append(s)

        b1.fillFromString(data)
#        b1.display(stop=True)

        ans = []
        solver.find_solution(b1,ans)

        if len(ans) != 0: 
            Board(ans[0]).show()
            self.fillTable(ans[0])
        else:
            print("no solution")

    def resetTable(self):
        table = self.ui.tableWidget
        for i in range(9):
            for j in range(9):
                table.item(i,j).setText("")
                table.item(i,j).setTextAlignment(QtCore.Qt.AlignCenter)
                table.item(i,j).setForeground(QtCore.Qt.green)
        table.viewport().update()


    def fillTable(self, bd):
        table = self.ui.tableWidget
        for i in range(9):
            for j in range(9):
                if bd[i][j]:
#                    print(f'({i},{j}) = {bd[i][j]}')
                    table.item(i,j).setText(str(bd[i][j]))
                    table.item(i,j).setTextAlignment(QtCore.Qt.AlignCenter)
                    table.item(i,j).setForeground(QtCore.Qt.green)
        table.viewport().update()

