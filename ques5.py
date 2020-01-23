# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 12:06:23 2020

@author: Roshan
"""

 
f = open("ques5.txt", "r") 
d = dict() 
for line in f:   
    line = line.strip() 
    line = line.lower() 
    words = line.split(" ") 
    for w in words:       
        if w in d:           
            d[w] = d[w] + 1
        else:            
            d[w] = 1
for key in list(d.keys()): 
    print(key, ":", d[key]) 
f.close()