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
# Solution 1

# 1. Initialize a variable called "length" to 0.
# 2. Traverse the string from the end using a loop.
# 3. When you encounter the first non-space character, set the "length" variable to 1.
# 4. Continue traversing the string and incrementing "length" until you encounter a space or reach the beginning of the string.
# 5. Return the value of "length".

def lengthOfLastWord(s):
    length = 0
    i = len(s) - 1
    
    while i >= 0:
        if s[i] != ' ':
            length += 1
        elif length > 0:
            return length
        i -= 1
        
    return length

print(lengthOfLastWord("hello world"))

# *******************************************************************************
# Solution 2

def lengthOfLastWord2(s):
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

print(lengthOfLastWord2("hello world"))