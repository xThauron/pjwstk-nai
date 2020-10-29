# Źródło: https://www.codingame.com/ide/puzzle/shadows-of-the-knight-episode-1
# Autor: Jakub Pilachowski (s17999)

import sys
import math

w, h = [int(i) for i in input().split()]
n = int(input())  
x0, y0 = [int(i) for i in input().split()]
x = x0
y = y0
w0 = 0
h0 = 0

while True:
    bomb_dir = input() 

    if bomb_dir == "U" or bomb_dir == "UR" or bomb_dir == "UL":
        h = y
        y = math.floor(y - ((y - h0) / 2))
    if bomb_dir == "D" or bomb_dir == "DR" or bomb_dir == "DL":
        h0 = y
        y = math.floor(y + ((h - y) / 2))
    if bomb_dir == "L" or bomb_dir == "UL" or bomb_dir == "DL":
        w = x
        x = math.floor(x - ((x - w0) / 2))
    if bomb_dir == "R" or bomb_dir == "UR" or bomb_dir == "DR":
        w0 = x
        x = math.floor(x + ((w - x) / 2))
    
    print(x, y, " ")
