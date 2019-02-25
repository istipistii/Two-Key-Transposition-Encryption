#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 21:44:03 2019

@author: manzars
"""
import numpy as np
class Encrypter:
    
    def remove_blank_space(self, message):
        msg = ''
        for i in range(len(message)):
            if(ord(message[i]) != 32):
                msg = msg + msg.join(message[i])
        return msg
    
    def making_x_and_y(self, msg):
        x, y = 0, 1
        for i in msg:
            x = x + (((ord(i) % 97) % 26) + 1)
        x = x % 26
        for i in msg:
            y = y * (((ord(i) % 97) % 26) + 1)
        y = y % 26
        return x,y
    
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
    
    def creating_first_ct(self, msg, gm, x_mat):
        first_ct = []
        k = 0
        for i in range(len(msg)):
            for j in range(25):
                if(msg[k] == gm[j]):
                    first_ct.append(x_mat[j])
                    k = k + 1
                    break
        first_ct = ''.join(str(x) for x in first_ct)
        return first_ct
    
    def making_ymat(self, y, x_mat):
        y_mat = []
        k = 0
        for i in range(y, 25):
            y_mat.append(x_mat[k])
            k = k + 1
        for i in range(0, y):
            y_mat.insert(i, x_mat[k])
            k = k + 1
        y_mat = np.asarray(y_mat)
        y_mat.resize(5, 5)
        y_mat = y_mat.T.ravel().tolist()
        return y_mat
    
    def creating_final_ct(self, first_ct, x_mat, y_mat):
        second_ct = []
        k = 0
        for i in range(len(first_ct)):
            for j in range(25):
                if(first_ct[k] == x_mat[j]):
                    second_ct.append(y_mat[j])
                    k = k + 1
                    break
        final_ct = ''.join(str(x) for x in second_ct)
        return final_ct
    
def main():
    msg = input("Enter the Text To Be Encrypted")
    encrypter = Encrypter()
    msg = encrypter.remove_blank_space(msg)
    x, y = encrypter.making_x_and_y(msg)
    gm = encrypter.making_global_matrix()
    x_mat = encrypter.making_xmat(x)
    first_ct = encrypter.creating_first_ct(msg, gm, x_mat)
    y_mat = encrypter.making_ymat(y, x_mat)
    final_ct = encrypter.creating_final_ct(first_ct, x_mat, y_mat)
    print("Message = {}\nEncrypted Text = {}\nfirst public key = {}\nsecond public key = {} ".format(msg, final_ct, format(x, 'b'), format(y, 'b')))
main()
