#!/usr/bin/python
# -*- coding: UTF-8 -*-

num=[]
for i in range(101,200):
    for j in range(2,i):
        if(i%j==0):
            break
        if(j==i-1):
            num.append(i)
print num
print 'The total is '+str(len(num))+''
