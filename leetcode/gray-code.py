# *******************************************************************************
# Question
# An n-bit gray code sequence is a sequence of 2^n integers where:
# - Every integer is in the inclusive range [0, 2^n - 1]
# - The first integer is 0
# - An integer appears no more than once in the sequence
# - The binary representation of every pair of adjacent integers differs by exactly one bit
# - The binary representation of the first and last integers differs by exactly one bit
# Given an integer n, return any valid n-bit gray code sequence.

# Example:
# Input: n = 2
# Output: [0,1,3,2]

# Explanation:
# The binary representation of [0,1,3,2] is [00,01,11,10].
# - 00 and 01 differ by one bit
# - 01 and 11 differ by one bit
# - 11 and 10 differ by one bit
# - 10 and 00 differ by one bit

# *******************************************************************************
# Solution
# 1. For n=1, return [0,1]
# 2. For n>1, generate the gray code sequence for n-1 recursively.
# 3. Reflect the gray code sequence of n-1 vertically, and add a '1' at the beginning of each number in the reflected sequence.
# 4. Combine the original gray code sequence of n-1 and the reflected gray code sequence to get the gray code sequence for n.

def grayCode(n: int) -> list[int]:
    if n == 1:
        return [0,1]
    prev_gray_code = grayCode(n-1)
    reflected_gray_code = [2**(n-1) + num for num in reversed(prev_gray_code)]
    return prev_gray_code + reflected_gray_code

print(grayCode(2)) # Output: [0, 1, 3, 2]

# Time Complexity: O(2^n)