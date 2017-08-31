#!/usr/bin/python
# -*- coding: UTF-8 -*-

num = []
a = 0
b = 1
num.append(a)
num.append(b)
for i in range(0,10):
    c = a+b
    d = b+c
    a = c
    b = d
    num.append(c)
    num.append(d)
print num
