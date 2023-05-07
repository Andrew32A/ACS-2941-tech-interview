# *******************************************************************************
# Question
# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

# You must implement a solution with a linear runtime complexity and use only constant extra space.

# Example:
# Input: nums = [4,1,2,1,2]
# Output: 4

# *******************************************************************************
# Solution 1

# 1. Initialize a variable called "result" to 0.
# 2. Traverse the array using a loop.
# 3. For each element in the array, use the XOR operation to update the value of "result" by XORing it with the element.
# 4. After the loop, "result" will contain the XOR of all the elements in the array.
# 5. Since the duplicates will cancel out, "result" will be left with the unique element.
# 6. Return the value of "result".

def singleNumber(nums):
    xor = 0
    for num in nums:
        xor ^= num
    
    return xor

numberList = [4, 1, 2, 1, 2]
print(singleNumber(numberList))

# Time complexity: O(n)