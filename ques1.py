# -*- coding: utf-8 -*-
"""
Spyder Editor

Print upper triangle of a square matrix and spiral of any matrix. 

This is a temporary script file.
"""

def upperMatrix():
    w, h = 3, 3;
    print("\n")
    Matrix = [ [1, 2, 3], 
          [7, 8, 9], 
          [13, 14, 15],
          ] 
    
    print (Matrix)
    for x in range(w):
        for y in range(h):
            if x<=y:
             print(Matrix[x][y], end=" "),
            else:
             print(" ", end=" "),
        print()
        
    print("\n")
        
    
    
    
    
def spiralMatrix(r, c, a) : 
    k = 0; l = 0
    while (k < r and l < c) : 
        for i in range(l, c) : 
            print(a[k][i], end = " ") 
        k += 1
        for i in range(k, r) : 
            print(a[i][c - 1], end = " ") 
        c -= 1
        if ( k < r) : 
            for i in range(c - 1, (l - 1), -1) : 
                print(a[r - 1][i], end = " ") 
            r -= 1
        if (l < c) : 
            for i in range(r - 1, k - 1, -1) : 
                print(a[i][l], end = " ")      
            l += 1

a = [ [1, 2, 3, 4, 5, 6], 
      [7, 8, 9, 10, 11, 12], 
      [13, 14, 15, 16, 17, 18],
      [19, 20, 21, 22, 23, 24]]      
r = 4; c = 6
spiralMatrix(r, c, a) 
upperMatrix()
