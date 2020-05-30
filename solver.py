import random
import numpy as np
import time
from curtsies import FullscreenWindow, fsarray, Input


def display(grid=None, stop=False, pause=0):
    if not grid:
        return
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
    
def printMatrix(grid):
    for i in range(9):
        print('----'*9)
        print('|', end=" ")
        for j in range(9):
            print(grid[i][j], end=' | ')
        print('')
    print('----'*9)



def possible(grid, i, j, n):
    for k in range(9):
        if grid[i][k] == n:
            return False

    for k in range(9):
        if grid[k][j] == n:
            return False

    bi = (i // 3)*3
    bj = (j // 3)*3
    for i in range(9):
        if grid[bi+i//3][bj+i % 3] == n:
            return False

    return True


def nSolve(grid, animated=False, sols=None):

    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                for n in range(1, 10):
                    if possible(grid, i, j, n):
                        grid[i][j] = n
                        if animated:
                            display(grid, pause=0.025)
                        nSolve(grid, animated, sols)
                        grid[i][j] = 0
                        if animated:
                            display(grid, pause=0.025)
                return
    if sols != None:
        sols.append([grid[i].copy() for i in range(9)])
    else:
        display(grid, stop=True)
    


def availNumbers(grid, i, j):
    nSet = {1,2,3,4,5,6,7,8,9}
    bi = i // 3
    bj = j // 3
    for k in range(9):
        if grid[i][k] in nSet:
            nSet.remove(grid[i][k])
        if grid[k][j] in nSet:
            nSet.remove(grid[k][j])
        if grid[bi*3+k//3][bj*3+k%3] in nSet:
            nSet.remove(grid[bi*3 + k//3][bj*3+k % 3])

    return nSet 

def oneSolve(grid):
    for l in range(81):
        i = l // 9
        j = l % 9
        if not grid[i][j]:
            s = availNumbers(grid, i, j)
            for n in s:
                grid[i][j] = n
                if not oneSolve(grid):
                    grid[i][j] = 0
                else:
                    return True
            return False
#    display(grid, stop=True)
    return True

def solveWithCountB(grid,bcnt,sols):
    for l in range(81):
        i, j = l // 9, l % 9
        if not grid[i][j]:
            s = availNumbers(grid, i, j)
            for n in s:
                grid[i][j] = n
                solveWithCountB(grid, bcnt,sols)
                bcnt += 1
                grid[i][j] = 0
            return 
    sols.append([grid[i].copy() for i in range(9)]) 

def uSolve(grid, animated=False,sols=None):
    for i in range(9):
        for j in range(9):
            if not grid[i][j]:
                s = availNumbers(grid, i, j)
                for n in s:
                    grid[i][j] = n
                    if animated:
                        display(grid, pause=0.015)
                    uSolve(grid, animated,sols)
                    grid[i][j] = 0
                    if animated:
                        display(grid, pause=0.015)
                return

    if sols != None:
        sols.append([grid[i].copy() for i in range(9)])
    else:
        display(grid, stop=True)


def find_solution(bd, sols):
    grid = bd.copyGrid()
#    printMatrix(grid)
#    nSolve(grid, False, sols)
    uSolve(grid,False,sols)


def sudoku_solve(bd):
    grid = bd.copyGrid()
    display(grid)
    nSolve(grid, False)

def random_puzzle(grid,reveal):
    cells = list(range(0, 80))
    numbers = list(range(1,10))

    for k in range(reveal):
        c = random.choice(cells)
        i = c // 9
        j = c  % 9
        while grid[i][j]:
            c = random.choice(cells)
            i = c // 9
            j = c  % 9
        
        n = random.choice(numbers)
        while not possible(grid,i,j,n):
            n = random.choice(numbers)
        
        print(f'{k}::grid[{i}][{j}] = {n}')
        grid[i][j] = n

def shuffle(l):
    t = l.copy()
    random.shuffle(t)
    return t

def prime_puzzle(grid):
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    random.shuffle(l)
    l1 = l[0:3]
    l2 = l[3:6]
    l3 = l[6:9]

    grid[0][0:3] = l1
    grid[0][3:6] = l2
    grid[0][6:9] = l3
    grid[1][0:3] = shuffle(l2)
    grid[1][3:6] = shuffle(l3)
    grid[1][6:9] = shuffle(l1)
    grid[2][0:3] = shuffle(l3)
    grid[2][3:6] = shuffle(l1)
    grid[2][6:9] = shuffle(l2)

def generate_puzzle(grid):
    prime_puzzle(grid)

#    display(grid,stop=True)
    oneSolve(grid)
#    display(grid,stop=True)
    printMatrix(grid)

    cells = [ i for i in range(81)]
    emptyCells = 0
    lastNum = 0
    lastVictim = -1
    while True:
        while True:
            victim = random.choice(cells)
            i, j = victim // 9, victim % 9
            if grid[i][j]:
                lastNum = grid[i][j]
                lastVictim = victim
                grid[i][j] = 0
                emptyCells += 1
                lastNum
                break
        
        ans = []
        bcnt = 0
        g  = [ grid[i].copy() for i in range(9)]
        solveWithCountB(g,bcnt,ans)

        scnt = len(ans)
#        print("solution cnt is ",len(ans))
        if scnt > 1:
            grid[lastVictim//9][lastVictim%9] = lastNum
            break

#        printMatrix(grid)
#        print('score is ',bcnt * 100 + emptyCells)

    printMatrix(grid)
    print('score is ',bcnt * 100 + emptyCells)

