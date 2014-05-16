'''
Created on May 15, 2014

@author: Quynh Doan
@question: Given two strings, check if one is an anagram/a permutation of the other.
@assumption: ASCII string (256 characters)
'''

def is_anagram(str1, str2):
    if len(str1) != len(str2):
        return False
    else:
        strLen = len(str1)
        char_count1 = char_count2 = [0]*256

        # Count the occurance of each letter
        for index in range(strLen):
            val1 = ord(str1[index])
            char_count1[val1] += 1

            val2 = ord(str2[index])
            char_count2[val2] += 1

        # Check if the two strings are anagrams
        for index in range(strLen):
            val1 = ord(str1[index])
            if char_count1[val1] != char_count2[val1]:
                return False
        return True
