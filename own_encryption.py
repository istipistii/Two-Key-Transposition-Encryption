#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 21:44:03 2019

@author: manzars
"""

msg = "ayan"
x = 0
y = 1

for i in msg:
    x = x + (((ord(i) % 97) % 26) + 1)
x = x % 26

for i in msg:
    y = y * (((ord(i) % 97) % 26) + 1)
y = y % 26

gm = []
for i in range(97, 123):
    gm.append(chr(i))
    
gm.pop(25)
x_mat = []
for i in range(25 - x, 25):
    x_mat.append(chr(i + 97))
    

for i in range(0, 25 - x):
    x_mat.append(chr(i + 97))

first_ct = []
k = 0
for i in range(len(msg)):
    for j in range(25):
        if(msg[k] == gm[j]):
            first_ct.append(x_mat[j])
            k = k + 1
            break


