'''
Created on May 15, 2014

@author: Quynh Doan
@requirements:  Replace all space in a string with anything.
                The default replacement string is '%20'.
'''

def replace_space(str1, rep = '%20'):
    mut_str = list(str1)
    for index in range(len(str1)):
        if mut_str[index] == ' ':
            mut_str[index] = rep
    return ''.join(mut_str)
