# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 13:09:13 2020

@author: Roshan
"""

arr=[-2,-4,1,7,3,-1,6]

sum=0
max=0
for i in range(0,len(arr)):
    sum+=arr[i]
    print(sum)
    if(sum<0):
        sum=0
    elif(sum>max):
        max=sum
print(max)