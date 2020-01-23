# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 12:42:34 2020

@author: Roshan
"""

def findsqrt(l,u,n):
    m=(l+u)/2
    sq=m*m;
    
    if((n==sq) or abs(n-sq)<0.0001):
        return m
    elif(sq<n):
        return findsqrt(m,u,n)
    else:
        return findsqrt(l,m,n)

print("Input a number to find its square root")
n=int(input())
for i in range(1,n):
    if i*i==n:
        res=i
        break
    elif i*i > n:
        res= findsqrt(i-1,i,n)
        break
    i=i+1
print(res)

    