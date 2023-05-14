# *******************************************************************************
# Question
# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.
# Notice that you may not slant the container.

# Example 1:
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

# Example 2:
# Input: height = [1,1]
# Output: 1

# *******************************************************************************
# Solution
# 1. Define a function called "maxArea" that takes a list of integers "height" as input.
# 2. Initialize two pointers, "left" and "right", at the start and end of the "height" list, respectively.
# 3. Initialize a variable "max_area" to 0.
# 4. While "left" is less than "right":
# 5. Calculate the area between the lines at "left" and "right" by multiplying the minimum value of "height[left]" and "height[right]" by the distance between the lines, which is "right - left".
# 6. Update "max_area" to be the maximum value between the current "max_area" and the area calculated in step 5.
# 7. Move the pointer with the shorter line inward.
# 8. Return "max_area".

def maxArea(height):
    left = 0
    right = len(height) - 1
    max_area = 0
    while left < right:
        area = min(height[left], height[right]) * (right - left)
        max_area = max(max_area, area)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_area

height = [1,8,6,2,5,4,8,3,7]
print(maxArea(height)) # 49

height = [1,1]
print(maxArea(height)) # 1

# Time complexity: O(n)