# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 02:58:10 2020

@author: Roshan
"""

import re

sentence= "My name is Tenet You can call me madam I speak Malayalam"
sentence=sentence.strip()
sentence=sentence.lower()
res=sentence.split(" ")
#res = re.findall(r'\w+', sentence.lower())
print ("The list of words is : " +  str(res)) 
array = []

array=res

max=0;
for i in range(0,len(array)):
    s=array[i]
    print(s)
    temp1=""
    for i in range(0,len(s)):
        
        temp1=temp1+s[len(s)-i-1]
    print(temp1)
    if s==temp1:
        length= len(s)
    else:
        length= 0
    if(length>max):
        max=length
print(max)

    

