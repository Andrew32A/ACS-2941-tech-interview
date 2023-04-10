# *******************************************************************************
# Question

# Given an integer x, return true if x is a palindrome, and false otherwise.

# Example 1:

# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.

# Example 2:
# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

# Example 3:
# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

# *******************************************************************************
# Solution 1

# 1. The integer x is passed as input to the function.
# 2. x is converted to a string: "121"
# 3. The string "121" is reversed using slice notation: "121" -> "121"
# 4. The reversed string "121" is stored in a variable called reversed_str.
# 5. The function compares the original string "121" to the reversed string "121", and finds that they are equal.
# 6. Since the two strings are equal, the function returns True, indicating that x = 121 is a palindrome.

def isPalindrome(x):
    reversed_str = str(x)[::-1]
    return str(x) == reversed_str

print(isPalindrome(121))