# *******************************************************************************
# Question

# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"

# Write the code that will take a string and make this conversion given a number of rows:

# string convert(string s, int numRows);
 

# Example 1:

# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"
# Example 2:

# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
# P     I    N
# A   L S  I G
# Y A   H R
# P     I
# Example 3:

# Input: s = "A", numRows = 1
# Output: "A"

# *******************************************************************************
# Solution 1

# 1. The function convert takes a string s and an integer numRows as input and returns a string representing s in a zigzag pattern with numRows rows.
# 2. If numRows is equal to 1, this means that the string cannot be converted to a zigzag pattern, so the function simply returns the original string s.
# 3. The function creates a list rows containing numRows empty strings, one for each row of the zigzag pattern.
# 4. The function initializes the variables row and direction. The variable row keeps track of the current row, and direction indicates whether we are moving up the rows or down the rows.
# 5. The function iterates over each character in the string s.
# 6. For each character, the function appends the character to the current row in the rows list.
# 7. The function then updates the row and direction variables. If we are at the top row (row == 0), we change direction to move down the rows (direction = 1). If we are at the bottom row (row == numRows - 1), we change direction to move up the rows (direction = -1). Otherwise, we simply continue in the current direction.
# 8. After iterating over all characters in s, the function concatenates the rows in the rows list into a single string using the join() method.
# 9. The function returns the final zigzag pattern string.

def convert(s, numRows):
    if numRows == 1:
        return s
    
    # create a list of empty strings, one for each row
    rows = ['' for _ in range(numRows)]
    
    # initialize the row and direction variables
    row = 0
    direction = 1
    
    # iterate over each character in the string
    for char in s:
        # append the character to the current row
        rows[row] += char
        
        # update the row and direction variables
        if row == 0:
            direction = 1
        elif row == numRows - 1:
            direction = -1
        row += direction
    
    # concatenate the rows into a single string
    return ''.join(rows)

print(convert("PAYPALISHIRING", 4))
