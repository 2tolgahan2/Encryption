#!usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 8 December 2019

Encryption wiht Key
@author: Tolgahan Bardakcı
@author-email: bardakcitolgahan@gmail.com
"""

__version__ = "0.1"
__author__ = "Tolgahan Bardakcı"
__url__ = "https://github.com/2tolgahan2/Encryption/blob/master/Encryption.py"

#add: try except!

key = 1202349
word = "selam"
word = word.lower()
word = word.replace(" ", "")

def listToString(final_list):
    # initialize an empty string
    str1 = ""
    # return string
    return (str1.join(final_list))

def encrypt():

    len_key = len(str(key))
    len_word = len(word)

    if(len_word % len_key == 0):
        repeat_time = int(len_word/len_key)
        range_of_loop = len(word)

        list_word = list(word)
        list_key = list(str(key))
        list_key = list_key * repeat_time

        final_list = []
        for i in range(len_word):
            value = list_key[i]
            letter = chr(ord(word[i]) + int(value))
            final_list.append(letter)

        res = listToString(final_list)
        print(res)
    else:
        repeat_time = int(len_word/len_key) + 1
        range_of_loop = len(word)

        list_word = list(word)
        list_key = list(str(key))
        list_key = list_key * repeat_time

        final_list = []
        for i in range(len_word):
            value = list_key[i]
            letter = chr(ord(word[i]) + int(value))
            final_list.append(letter)

        res = listToString(final_list)
        print(res)

encrypt()
