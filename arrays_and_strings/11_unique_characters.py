'''
Created on May 14, 2014

@author: Quynh Doan
'''

def has_uniq_char(words):
    # Has more words than the number of ASCII characters
    if len(words) > 256:
        return False
    else:
        char_set = [False]*256
        for index in range(len(words)):
            char_val = ord(words[index])
            if char_set[char_val] is True:
                return False
            else:
                char_set[char_val] = True
        return True
