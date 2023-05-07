import re

# *******************************************************************************
# Question
# Given a string s consisting of words and spaces, return the length of the last word in the string.

# A word is a maximal 
# substring
# consisting of non-space characters only.

def lengthOfLastWorld(s):
    # variable named count/length
    length = 0

    # len(s) - 1
    i = len(s) - 1

    while i >= 0:
        if s[i].isalpha() == True or s[i] == "-" or s[i].isnumeric():
            length += 1
        elif length > 0:
            return length
        i -= 1

    return length

print(lengthOfLastWorld("hello (7-eleven)."))



