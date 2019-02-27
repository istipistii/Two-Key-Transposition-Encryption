#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 00:53:03 2019

@author: manzars
"""
import numpy as np

class Decrypter:
    
    def making_global_matrix(self):
        gm = []
        for i in range(97, 123):
            gm.append(chr(i))
        gm.pop(25)
        return gm
    
    def making_xmat(self, x):
        x_mat = []
        for i in range(25 - x, 25):
            x_mat.append(chr(i + 97))
        for i in range(0, 25 - x):
            x_mat.append(chr(i + 97))
        return x_mat
    
    def making_ymat(self, i, j, x_mat):
        y_mat, a, b = [], i, j
        for temp in range(25):
            y_mat.append("*")
        y_mat = np.asarray(y_mat)
        y_mat = y_mat.reshape(5, 5)
        x,y = a, b
        for p in range(5):
            if(((a + p) % 5) == 0):
                break
        a, b = (a+p)%5, (b+1)%5
        q, k  = 0, 0
        for j in range(b, b+5):
            for i in range(a, a+5):
                y_mat[i%5][j%5] = x_mat[q + p]
                k = k + 1
                q = q + 1
                if((k + p) == 25):
                    break
        q = 0
        while(p != 0):
            y_mat[x][y] = x_mat[q]
            x = x + 1
            p = p - 1
            q = q + 1
        return y_mat.ravel().tolist()

    def calculate_index(self, y):
        k = 0
        for i in range(5):
            for j in range(5):
                if(k == y):
                    return i,j
                k = k + 1
    
    def decrypting_first_ct(self, msg, y_mat, x_mat):
        second_ct = []
        k = 0
        for i in range(len(msg)):
            for j in range(25):
                if(msg[k] == y_mat[j]):
                    second_ct.append(x_mat[j])
                    k = k + 1
                    break
        final_ct = ''.join(str(x) for x in second_ct)
        return final_ct
    
    def decrypting_second_ct(self, first_ct, gm, x_mat):
        final_ct = []
        k = 0
        for i in range(len(first_ct)):
            for j in range(25):
                if(first_ct[k] == x_mat[j]):
                    final_ct.append(gm[j])
                    k = k + 1
                    break
        final_ct = ''.join(str(x) for x in final_ct)
        return final_ct
   
def main():
    msg = input("Enter the message to Decrypt:\n")
    x, y = input("Enter the first public key:\n"), input("Enter the second public key:\n")
    x = int(str(x), 2)
    y = int(str(y), 2)
    
    decrypter = Decrypter()
    gm = decrypter.making_global_matrix()
    x_mat = decrypter.making_xmat(x)
    i, j = decrypter.calculate_index(y)
    y_mat = decrypter.making_ymat(i, j, x_mat)
    first_ct = decrypter.decrypting_first_ct(msg, y_mat, x_mat)
    decpt = decrypter.decrypting_second_ct(first_ct, gm, x_mat)
    print("Encrypted text = {}\nDecrypted Text = {}\n".format(msg, decpt))
main()

 