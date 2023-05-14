# *******************************************************************************
# Question
# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Example 1:
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Example 2:
# Input: strs = [""]
# Output: [[""]]

# Example 3:
# Input: strs = ["a"]
# Output: [["a"]]
# *******************************************************************************

# Solution
# 1. Define a function called "groupAnagrams" that takes a list of strings "strs" as an input.
# 2. Initialize a dictionary called "anagrams" to an empty dictionary.
# 3. Traverse the strings in the list "strs" using a loop.
# 4. For each string in "strs", sort its characters and store it as a tuple called "key".
# 5. If "key" is not already in the dictionary "anagrams", add it as a key with an empty list as its value.
# 6. Append the original string to the list corresponding to "key" in the dictionary "anagrams".
# 7. Return the values of the dictionary "anagrams" as a list.

def groupAnagrams(strs):
    anagrams = {}
    for s in strs:
        key = tuple(sorted(s))
        if key not in anagrams:
            anagrams[key] = []
        anagrams[key].append(s)
    return list(anagrams.values())

strings = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strings))


# Time complexity: O(nklog(k)) where n is the number of strings in "strs" and k is the maximum length of a string. The sorting of the characters takes O(k*log(k)) time and it is done for each of the n strings.