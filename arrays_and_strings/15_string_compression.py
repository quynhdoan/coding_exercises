'''
Created on May 15, 2014

@author: Quynh Doan
@reqs:  Implement a method to perform basic string compression
        using the counts of repeated charactes. If the compressed 
        string would not become smaller than the original string, 
        the method should return the original string.
@assumption: ASCII (256 characters)
'''

import 11_unique_characters

def str_compress(str1):
    # No duplicate character
    if has_uniq_char(str1) is True:
        return str1
    else:
        char_count = [0]*256
        com_str = list()

        # Count the occurance of each letter
        for index in range(len(str1)):
            val = ord(str1[index])
            char_count[val] += 1

        # Add to the list of compressed chars
        for index in range(256):
            if char_count[index] > 0:
                com_str.append(chr(index))
                com_str.append(str(char_count[index]))

        return ''.join(com_str)