# *******************************************************************************
# Question

# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

# Example:
# Input: strs = ["flower","flow","flight"]
# Output: "fl"

# *******************************************************************************
# Solution 1

# 1. Define a function called "longestCommonPrefix" that takes a list of strings "strs" as an input.
# 2. Check if the list "strs" is empty. If it is, return an empty string.
# 3. Find the shortest string in the list "strs" using the built-in "min" function and store it in a variable called "shortest".
# 4. Traverse the characters in the "shortest" string using a loop and an index variable "i".
# 5. For each character at index "i" in the "shortest" string, compare it with the character at the same index in each of the other strings in the list "strs" using a nested loop.
# 6. If any of the characters in the other strings at index "i" do not match the character at index "i" in the "shortest" string, return a substring of "shortest" that includes all the characters up to index "i".
# 7. If all the characters at index "i" match in all the strings in the list "strs", continue traversing until the end of the "shortest" string is reached.
# 8. If the loop completes without finding a difference in any of the strings, return the entire "shortest" string as the longest common prefix.

def longestCommonPrefix(strs):
    if not strs:
        return ""
    shortest = min(strs,key=len)
    for i, ch in enumerate(shortest):
        for other in strs:
            if other[i] != ch:
                return shortest[:i]
    return shortest 

strings = ["flower","flow","flight"]
print(longestCommonPrefix(strings))