#!usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 14 December 2019

Decryption with Key
@author: Tolgahan Bardakcı
@author-email: bardakcitolgahan@gmail.com
"""

__version__ = "0.1"
__author__ = "Tolgahan Bardakcı"
__url__ = "https://github.com/2tolgahan2/Encryption/blob/master/Encryption.py"

#from getpass import getpass
#import textract

key = 111
word = "ifmmp!xpsme"

try:
    word = str(word)
except:
    raise TypeError
    print("Please check the type of the input")

word = word.lower()

def listToString(final_list):
    str1 = ""
    return (str1.join(final_list))

len_key = len(str(key))
len_word = len(word)
range_of_loop = len(word)

list_word = list(word)
list_key = list(str(key))

    
def decrypt():
    global list_key
    if(len_word % len_key == 0):
        repeat_time = int(len_word/len_key)
        list_key = list_key * repeat_time

        final_list = []
        for i in range(len_word):
            value = list_key[i]
            letter = chr(ord(word[i]) - int(value))
            final_list.append(letter)

    else:
        repeat_time = int(len_word/len_key) + 1
        list_key = list_key * repeat_time

        final_list = []
        for i in range(len_word):
            value = list_key[i]
            letter = chr(ord(word[i]) - int(value))
            final_list.append(letter)

    res = listToString(final_list)
    result_file = open("En_Result.txt", "w")

    print(res, file=result_file, flush="True")
    result_file.close()
    print("Your text is printed to the file 'En_Result.txt' ")

decrypt()