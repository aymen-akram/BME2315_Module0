# This is your first coding assignment for Computational BME.
# As discussed in class, feel free to use AI tools to help you complete this assignment, but remember to cite them.
# I encourage you to try the problems yourself first and only use AI tools when you are stuck to benefit your learning. 

# %% ###########################################################
# Problem 1: Practice writing pseudocode

# Write pseudocode that will input a integer N and output the sum of the first N numbers in the fibonacci sequence.
# Fibonacci sequence starts: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...
# Example: If N = 5, the output should be 0 + 1 + 1 + 2 + 3 = 7

""" # you can use three double-quotes to write multi-line comments
INPUT an integer N

SET a = 0, b = 1 
SET count = 0
SET total = 0

WHILE count is less than N
    ADD a to the total 
    SET the next_val = a + b
    SET a = b
    SET b = next_val
    increase the count by 1 

OUTPUT total 
"""

# %% ###########################################################
# Problem 2: Comment your code
# Comments are very helpful for others (especially when pair-coding!) and yourself to understand your code! Add comments to the following code, which will run but produces the wrong output. Once you comment the code, you should be able to identify the error and fix it (the correct total that should be printed is 12).
N = 6 # the amount of Fibonacci numbers that will be summed 

a = 0 # set a to the first fibonacci number
b = 1 # set b to the second fibonacci number
count = 0 # keeps track of how many Fibonacci numbers have been added so far 
total = 0 # stores the total sum 

while count < N: # while the count is less than N which is 6
    total = total + a # Error because originally it said "total = total + b" which had skipped the first number. Now it is fixed by starting with a 

    next_value = a + b # calculates the next fibonacci number 
    a = b # moves a forward 
    b = next_value # makes b the next value 

    count = count + 1 # moves to the next term by increasing the count by 1 

print(total) # prints the total sum 

# %% ###########################################################
# Problem 3: Using common Python libraries
# What is the standard deviation of the first 10 numbers in the fibonacci sequence? Use the numpy library to calculate the standard deviation.

import numpy as np 
fibonacci_numbers = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
standard_deviation = np.std(fibonacci_numbers)
print(fibonacci_numbers)
print(standard_deviation)

# %% ###########################################################
# Problem 4: Don't repeat yourself by writing functions
# Write a function that takes an integer N as input and returns the sum of the first N numbers in the fibonacci sequence.
# Then use this function to calculate the sums for N = 5, 10, 15, 20, 25, and 30 and print them as a list.

def sum_fibonacci(N):
    a = 0 
    b = 1
    count = 0
    while count < N:
        total = total + a  
        a, b = b, a + b 
        count = count + 1
    return total  
N_values = [5, 10, 15, 20, 25, 30]
sums = []
for N in N_values: 
    sums.append(sum_fibonacci(N))
print(sums)

# %% ###########################################################
# Problem 5: Read your error messages
# Run the following code block to see what the error messages are. Then, for each error:
# 1. Identify what type of error it is (SyntaxError, NameError, TypeError, etc.)
# 2. Add a comment to the line that is throwing the error explaining what the error is
# 3. Fix the error so that the code runs correctly

# You will only see one error at a time when you run the code. After fixing one error, run the code again to see the next error. Your final code should work correctly and will have comments where the original errors were.


def find_fib_above_limit(limit):
    """# The function inputs an integer called "limit" and finds the first number that goes above "limit" in the fibonacci sequence. It returns the index of that number.
    :param limit: limit of fibonacci sequence
    :type limit: integer
    :return: index of the first number above limit
    :rtype: integer
    """
    a = 0 # it was a = "0" before which was a TypeError because you can not compare an integer with a string. Therefore, the <= was not supported 
    b = 1 # same as above 
    index = 0 # index was not initialized before which caused a NameErrror

    while a <= limit:
        next_value = a + b
        a = b
        b = next_value
        index += 1

    return index


result = find_fib_above_limit(50)
print("The index of the first number above your limit is: ", result)
# %% ###########################################################
# Problem 6: Test your code
# The following function will run but will output the wrong answer sometimes. Add test cases to verify that the function works correctly for a variety of inputs. If you find any inputs that produce incorrect outputs, fix the function. The function, when working properly, should return the sum of all odd Fibonacci numbers less than or equal to the input "limit".


def sum_even_fib(limit):
    a, b = 0, 1
    total = 0
    while b <= limit:
        if b % 2 == 0:  # This line checks if the Fibonacci number is even
            total += b # This line was originally "total = +b" which was incorrect because it only assigns the value of b to total instead of adding it. The correct line should be "total += b" to get the sum of even Fibonacci numbers.
        a, b = b, a + b
    return total


# Add your test cases here
print(sum_even_fib(0))    # will get 0
print(sum_even_fib(9))    # will get 10
print(sum_even_fib(10))   # will get 10
print(sum_even_fib(11))   # will get 10
print(sum_even_fib(100))  # will get 44

# %%
