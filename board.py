import random
import numpy as np
import time
from curtsies import FullscreenWindow, fsarray, Input

class Board:
    def __init__(self,grid = None):
        self.bd = [ [0]*9 for _ in range(9)]
        if grid and (len(grid) == 9) and (len(grid[0])  == 9):
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

    def display(self,grid=None,stop=False,pause=0):
        if not grid: grid = self.bd
        m = ["-"*30]
        for r in grid:
            mm = "|"
            for e in r:
                mm = mm + ' ' + (str(e) if e else ' ') + ' '
            mm += '|'
            m.append(mm)
        m.append("-"*30)

        if stop:
            m.append("Hit any key to see more")

        with Input() as input:
            with FullscreenWindow() as win:
                win.render_to_terminal(fsarray(m))
                if stop:
                    c = input.next()
                if not pause:
                    time.sleep(pause)

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

    def possible(self, i, j, n):
        for k in range(9):
            if self.bd[i][k] == n:
                return False

        for k in range(9):
            if self.bd[k][j] == n:
                return False

        bi = (i // 3)*3
        bj = (j // 3)*3
        for i in range(9):
            if self.bd[bi+i//3][bj+i%3] == n:
                    return False

        return True

    def sudoku_solve(self):
        def solve(grid,animated=False):
            for i in range(9):
                for j in range(9):
                    if grid[i][j] == 0:
                        for n in range(1, 10):
                            if self.possible(i, j, n):
                                grid[i][j] = n
                                if animated: self.display(grid,pause=0.025)
                                solve(grid,animated)
                                grid[i][j] = 0
                                if animated: self.display(grid,pause=0.025)
                        return
            self.display(grid,stop=True)
        
        solve(self.bd,False)


    def random(self):
        choice = list(range(1, 10))
        for i in range(9):
            for j in range(9):
                self.bd[i][j] = random.choice(choice)

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


if __name__ == "__main__":
    grid = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]]
    grid0 = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 0, 0]]

    grid1 = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 6, 0, 1, 0, 7, 3, 0, 0],
        [1, 2, 0, 0, 5, 0, 0, 0, 8],
        [0, 0, 8, 7, 0, 1, 0, 0, 6],
        [0, 7, 0, 0, 0, 0, 0, 1, 0],
        [4, 0, 0, 9, 0, 8, 2, 0, 0],
        [5, 0, 0, 0, 8, 0, 0, 7, 4],
        [0, 0, 4, 5, 0, 3, 0, 6, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]]
    grid2 = [[3, 0, 0, 9, 8, 2, 0, 1, 0],
        [2, 1, 5, 7, 0, 0, 4, 8, 9],
        [0, 9, 0, 0, 5, 0, 2, 6, 3],
        [7, 0, 0, 0, 9, 0, 1, 0, 6],
        [1, 5, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 3, 0, 7, 0, 0, 0, 2],
        [0, 8, 0, 0, 4, 0, 0, 2, 1],
        [0, 0, 1, 8, 2, 9, 6, 0, 0],
        [0, 0, 0, 5, 1, 0, 0, 0, 8]]

    b = Board(grid0)
    # b.random()
    # b.disp()
    # b.fakeValid()
    # b.reset()
    # b.disp()
    # b.fill()
    b.display(stop=True)
    b.sudoku_solve()

