# *******************************************************************************
# Question
# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

# Example:
# Input: nums = [2,2,1,1,1,2,2]
# Output: 2

nums = [2,2,1,1,1,2,2] # 2
nums = [1,2,3,4,5,6,7] # none
nums = [1] # 1

# define function x
# store array in nums_len x
# num_hash dict/hash to store frequency x
# loop over array
# check to see if in num_hash, if not, append to it
# ⌊n / 2⌋, return majority element

def majorityFunction(nums):
    num_len = len(nums)
    num_hash = {}

    for num in nums:
        num_hash[num] = num_hash.get(num, 0) + 1
        if num_hash[num] > num_len / 2:
            return num
        
testList = [1]
print(majorityFunction(testList))

