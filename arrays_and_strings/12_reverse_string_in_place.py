'''
Created on May 15, 2014

@author: Quynh Doan
@usage: reverse a list of characters in place
'''

def reverse_str(inputStr):
    strLen = len(inputStr)
    outputStr = list(inputStr)

    for index in range(0, strLen/2):
        temp = outputStr[strLen-index-1]
        outputStr[strLen-index-1] = outputStr[index]
        outputStr[index] = temp

        # Shorter solution: the Python way
        # outputStr[strLen-index-1], outputStr[index] = outputStr[index], outputStr[strLen-index-1]
    return ''.join(outputStr)