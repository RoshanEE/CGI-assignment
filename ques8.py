# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 12:42:02 2020

@author: Roshan
"""

def sorting(a,b):
    l2=len(b)
    ctr1=0
    ctr=3 
    x=0
    while (x<=ctr):
        for y in range(ctr1,l2):     
            if b[y]<a[x]:
                ctr=ctr+1              
                ctr1=ctr1+1
                for z in reversed(range(x,ctr+1)):                  
                    a[z+1]=a[z]                               
                a[x]=b[y]
                print(a)
        x=x+1  
a=[1,4,7,9,None,None,None,None]
b=[2,3,8]
sorting(a,b)