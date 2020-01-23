# -*- coding: utf-8 -*-
"""
Spyder Editor

Print upper triangle of a square matrix and spiral of any matrix. 

This is a temporary script file.
"""
w, h = 3, 3;
Matrix = [[0 for x in range(w)] for y in range(h)] 
Matrix[0][0] = 1
Matrix[0][1] = 2
Matrix[0][2] = 3
Matrix[1][0] = 4
Matrix[1][1] = 5
Matrix[1][2] = 6
Matrix[2][0] = 7
Matrix[2][1] = 8
Matrix[2][2] = 9

print (Matrix)
for x in range(w):
    for y in range(h):
        if x<=y:
         print(Matrix[x][y], end=" "),
        else:
         print(" ", end=" "),
    print()