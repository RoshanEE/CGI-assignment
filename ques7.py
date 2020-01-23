# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 10:29:00 2020

@author: Roshan
"""
   
def permutation(arr, l, u): 
    if l==u: 
        print (toString(arr)) 
    else: 
        for i in range(l,u+1): 
            arr[l], arr[i] = arr[i], arr[l] 
            permutation(arr, l+1, u) 
            arr[l], arr[i] = arr[i], arr[l] 
            
def toString(List): 
    return ''.join(List) 
  
string = "CGI"
arr = list(string)
n = len(string) 
permutation(arr, 0, n-1) 