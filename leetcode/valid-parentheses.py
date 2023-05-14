# ******************************************************************************
# Problem:
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.
# An input string is valid if:
# 1. Open brackets must be closed by the same type of brackets.
# 2. Open brackets must be closed in the correct order.
# 3. Every close bracket has a corresponding open bracket of the same type.

# Examples:
# Input: s = "()"
# Output: true
# Input: s = "()[]{}"
# Output: true
# Input: s = "(]"
# Output: false

# ******************************************************************************
# Solution:
# We can use a stack to keep track of the opening brackets encountered in the string.
# Whenever we encounter a closing bracket, we check if it matches the top element
# of the stack. If it does, we pop the element from the stack and continue iterating.
# If it doesn't match, we return False, as the string is not valid.
# At the end, we check if the stack is empty or not. If it is empty, we return True,
# else we return False.

def isValid(s: str) -> bool:
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in mapping:
            if not stack or stack[-1] != mapping[char]:
                return False
            stack.pop()
        else:
            stack.append(char)
    return not stack

print(isValid("()")) # True
print(isValid("()[]{}")) # True
print(isValid("(]")) # False

# Time complexity: O(n)