from solver import sudoku_solve, display, possible
import random


class Board:
    def __init__(self, grid=None):
        self.bd = [[0]*9 for _ in range(9)]
        if grid and (len(grid) == 9) and (len(grid[0]) == 9):
            for i in range(9):
                for j in range(9):
                    self.bd[i][j] = grid[i][j]

    def show(self):
        for i in range(9):
            print('----'*9)
            print('|', end=" ")
            for j in range(9):
                print(self.bd[i][j], end=' | ')
            print('')
        print('----'*9)

    def display(self, stop=False):
        display(self.bd, stop)

    def solve(self):
        sudoku_solve(self)

    def reset(self):
        for i in range(9):
            for j in range(9):
                self.bd[i][j] = 0

    def fill(self):
        choice = list(range(1, 10))
        for i in range(9):
            for j in range(9):
                c = random.choice(choice)
                while not self.possible(i, j, c):
                    c = random.choice(choice)
                print(f'filled ({i},{j}) with ({c})')
                self.bd[i][j] = c

    def fillFromString(self, numstr):
        if len(numstr) != 9:
            print("Not a valid number of rows")
            return

        for i, n in enumerate(numstr):
            if len(n) != 9:
                print("Not enough column in row ", i)
                return
            for j, c in enumerate(n):
                self.bd[i][j] = int(c)

    def copyGrid(self):
        return [self.bd[i].copy() for i in range(9)]




    def fakeValid(self):
        for i in self.bd:
            print(f'{i}th row : ', sum(i))

        for i in zip(*self.bd):
            print(f'{i}th col : ', sum(i))

        for i in range(3):
            temp = self.bd[slice(i*3, (i+1)*3)]
            for j in range(3):
                subm = [row[slice(j*3, (j+1)*3)] for row in temp]
                s = 0
                for k in range(3):
                    s += sum(subm[k])
                print(f'submatrix\'s sum: : {s}')

    def isValid(self):
        for i in self.bd:
            if sum(i) != 45:
                return False

        for i in zip(*self.bd):
            if sum(i) != 45:
                return False

        for i in range(3):
            temp = self.bd[slice(i*3, (i+1)*3)]
            for j in range(3):
                subm = [row[slice(j*3, ((j+1))*3)]
                        for row in temp]
                s = 0
                for k in range(3):
                    s += sum(subm[k])
                if s != 45:
                    return False
