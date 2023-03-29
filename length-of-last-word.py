# *******************************************************************************
# Question
# Given a string s consisting of words and spaces, return the length of the last word in the string.

# A word is a maximal 
# substring
# consisting of non-space characters only.

# Example 1:
# Input: s = "Hello World"
# Output: 5
# Explanation: The last word is "World" with length 5.

# *******************************************************************************
# Solution

def lengthOfLastWord(s):
    ls = len(s)
    # slow and fast pointers
    slow = -1
    # iterate over trailing spaces
    while slow >= -ls and s[slow] == ' ':
        slow-=1
    fast = slow
    # iterate over last word
    while fast >= -ls and s[fast] != ' ':
        fast-=1
    return slow - fast

print(lengthOfLastWord("hello world"))