# *******************************************************************************
# Question

# Given an array of integers nums, return the second smallest element in the array. If there is no second smallest element, return -1.

# Example 1:
# Input:
# nums = [5, 8, 1, 3, 9, 7]

# Output:
# 3

# Example 2:
# Input:
# nums = [4, 2, 2, 4, 3]

# Output:
# 3

# Example 3:
# Input:
# nums = [2]

# Output:
# -1

# *******************************************************************************
# Solution 1

# 1. Remove duplicates from the array
# 2. Sort the array in increasing order
# 3. If the length of the array is less than 2, return -1. Otherwise, return the element at index 1

def find_second_smallest(nums):
    nums = list(set(nums))
    nums.sort()
    if len(nums) < 2:
        return -1
    else:
        return nums[1]

nums1 = [5, 8, 1, 3, 9, 7]
nums2 = [4, 2, 2, 4, 3]
nums3 = [2]
print(find_second_smallest(nums1)) # should print 3
print(find_second_smallest(nums2)) # should print 3
print(find_second_smallest(nums3)) # should print -1