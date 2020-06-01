import sys
from PyQt5.QtWidgets import QApplication
from gui import SudokuWindow


def main():
    app = QApplication(sys.argv)
    window = SudokuWindow()

    window.show()
    sys.exit(app.exec_())

'''
TODO : add interactive function for solving puzzles.
'''

main()

