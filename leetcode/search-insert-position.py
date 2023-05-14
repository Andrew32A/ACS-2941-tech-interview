# *******************************************************************************
# Question
# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
# You must write an algorithm with O(log n) runtime complexity.
# Example 1:
# Input: nums = [1,3,5,6], target = 5
# Output: 2
# Example 2:
# Input: nums = [1,3,5,6], target = 2
# Output: 1
# Example 3:
# Input: nums = [1,3,5,6], target = 7
# Output: 4
# *******************************************************************************
# Solution
# Approach:
# We can use binary search to solve the problem. We initialize two pointers, low and high, to the first and last index of the array respectively. We then keep calculating the mid index until we find the target or we cannot further narrow down the search. If we find the target, we simply return the mid index. Otherwise, we return the index where it would be if it were inserted in order, which is the low index.

def searchInsert(nums, target):
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return low

nums = [1,3,5,6]
target = 5
print(searchInsert(nums, target)) # 2

target = 2
print(searchInsert(nums, target)) # 1

target = 7
print(searchInsert(nums, target)) # 4


# Time Complexity: O(log n)