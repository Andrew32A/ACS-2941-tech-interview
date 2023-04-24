# *******************************************************************************
# Question
# Given an integer n, return a string array answer (1-indexed) where:

# answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
# answer[i] == "Fizz" if i is divisible by 3.
# answer[i] == "Buzz" if i is divisible by 5.
# answer[i] == i (as a string) if none of the above conditions are true.
 
# Example 1:
# Input: n = 3
# Output: ["1","2","Fizz"]

# *******************************************************************************
# Solution 1

# step 1: create function that takes in number
# step 2: iterate that incriments from 1 to input number
# step 3: check if divisible by 3 and 5 first, if so return "FizzBuzz"
# step 4: check if divisible by 3, if so return "Fizz"
# step 5: check if divisible by 5, if so return "Buzz"
# step 6: else, return number

def fizzBuzz(n):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
        
fizzBuzz(15)

# Time complexity: O(n)

# *******************************************************************************
# Solution 2 (ternary)
def fizzBuzz2(n):
    return ['Fizz' * (not i % 3) + 'Buzz' * (not i % 5) or str(i) for i in range(1, n+1)]

print(fizzBuzz2(15))
