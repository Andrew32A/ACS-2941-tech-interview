# *******************************************************************************
# Question
# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

# Example:
# Input: nums = [2,2,1,1,1,2,2]
# Output: 2

# *******************************************************************************
# Solution 1

# 1. Define a function called "majorityElement_hash" that takes an array "nums" as an input.
# 2. Get the length of the array "nums" and store it in a variable called "num_len".
# 3. Initialize an empty hash table called "num_hash" to keep track of the frequency of each element in the array.
# 4. Traverse the array using a loop.
# 5. For each element in the array, check if it already exists in the "num_hash" hash table.
# 6. If it does, increment the corresponding frequency by 1.
# 7. If it doesn't, add the element to the "num_hash" hash table with a frequency of 1.
# 8. While traversing the array, check if the frequency of any element is greater than "num_len" divided by 2.
# 9. If it is, return the element as the majority element.
# 10. If the loop completes without finding a majority element, return None or any value that represents that no majority element exists.

def majorityElement_hash(nums):
    num_len = len(nums)
    num_hash = {}
    for num in nums:
        num_hash[num] = num_hash.get(num, 0) + 1
        if num_hash[num] > num_len/2:
            return num

nums = [2,2,1,1,1,2,2]
print(majorityElement_hash(nums))

# Time complexity: O(n)