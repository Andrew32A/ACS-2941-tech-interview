# Practice Problems:

# Find the k largest values in an array of n numbers. Return them in a new array sorted in decreasing order.

def find_k_largest(arr, k):
    """
    Given an array of n numbers, finds the k largest values and returns them in a new array sorted in decreasing order.
    
    Args:
    - arr: a list of n numbers
    - k: an integer representing the number of largest values to return
    
    Returns:
    - a list of k largest values in arr, sorted in decreasing order
    """
    arr.sort(reverse=True) # sort the array in descending order
    return arr[:k] # return the first k elements of the sorted array

arr = [3, 5, 2, 8, 1, 9, 4, 7, 6]
k = 3
largest_values = find_k_largest(arr, k)
print(largest_values) # Output: [9, 8, 7]

# Given an array a of numbers and a target value t, find two numbers that sum to t (that is, a[i] + a[j] = t).

def find_sum_pair(arr, target):
    """
    Given an array of numbers and a target value, finds two numbers that sum to the target value and returns their indices.
    
    Args:
    - arr: a list of n numbers
    - target: the target value to find the sum pair for
    
    Returns:
    - a tuple containing the indices of the two numbers that sum to the target value, or None if no such pair exists
    """
    n = len(arr)
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] + arr[j] == target:
                return (i, j)
    return None # no sum pair exists

arr = [2, 5, 7, 11, 15]
target = 9
indices = find_sum_pair(arr, target)
print(indices) # Output: (0, 1)

# Given a list of n strings with mixed casing, return a new list of all strings that start with a capitalized letter.

def get_capitalized_strings(lst):
    """
    Given a list of n strings with mixed casing, returns a new list of all strings that start with a capitalized letter.
    
    Args:
    - lst: a list of n strings
    
    Returns:
    - a new list containing all strings in lst that start with a capitalized letter
    """
    return [s for s in lst if s[0].isupper()]

lst = ['Apple', 'banana', 'Carrot', 'doughnut', 'Egg']
new_lst = get_capitalized_strings(lst)
print(new_lst) # Output: ['Apple', 'Carrot', 'Egg']


# Find the longest substring of unique letters in a given string of n letters.

def longest_unique_substring(s):
    """
    Given a string s of n letters, finds the longest substring of unique letters and returns it.
    
    Args:
    - s: a string of n letters
    
    Returns:
    - the longest substring of unique letters in s
    """
    n = len(s)
    max_substring = ""
    substring = ""
    i = 0
    j = 0
    char_set = set()
    while j < n:
        if s[j] not in char_set:
            char_set.add(s[j])
            substring = s[i:j+1]
            j += 1
        else:
            char_set.remove(s[i])
            i += 1
        if len(substring) > len(max_substring):
            max_substring = substring
    return max_substring

s = "abcabcbb"
longest_substring = longest_unique_substring(s)
print(longest_substring) # Output: "abc"
