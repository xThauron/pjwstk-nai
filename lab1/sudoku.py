# Źródło: https://www.codingame.com/ide/puzzle/sudoku-solver
# Autor: Jakub Pilachowski (s17999)

import sys
import math

def used_in_row(board, num, row):
    for i in range(9):
        if board[row][i] == num:
            return True
    return False

def used_in_column(board, num, column):
    for i in range(9):
        if board[i][column] == num:
            return True
    return False

def used_in_box(board, num, row, column):
    row = row - row % 3
    column = column - column % 3
    for i in range(3):
        for j in range(3):
            if board[i+row][j+column] == num:
                return True
    return False

def is_field_save(board, num, row, column):
    return not used_in_row(board, num, row) and not used_in_column(board, num, column) and not used_in_box(board, num, row, column)

def solve_sudoku(board):
    row = 0
    column = 0
    found = False

    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                row = i
                column = j
                found = True
                break
        if found:
            break
    if not found:
        return True
    for num in range(1, 10):
        if is_field_save(board, num, row, column):
            board[row][column] = num
            if(solve_sudoku(board)):
                return True

        board[row][column] = 0
    return False

board = []
for i in range(9):
    line = input()
    board.append([])
    for j in range(9):
        board[i].append(int(line[j]))

if solve_sudoku(board):
    for i in range(9):
        print(''.join(map(str, board[i])))
else:
    print("No solution")
