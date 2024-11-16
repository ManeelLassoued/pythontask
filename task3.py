#Problem Solving:
#How to accept multiple inputs in a line
# Sometimes we have to accept multiple inputs in a single line.The way to accept multiple integers in a single line is to use the split and map function.
# split function breaks the input based on the separator - by default, it splits inputs separated by spaces in a single line into different inputs which you can assign to different variables
# map function converts each input into the defined datatype
# The syntax for the same is as follows -
# a, b, c = map(int, input().split())   # assigns integer input values to variables a, b and c

# In this code, we take input using input(), then split it using input().split().
# Once the input is split, we convert each value into a integer using map.
# Task
# Now lets try and solve the following
# Accept 3 space separated integers given in a line into 3 variables - A, B and C
# Print them out to a single line on the console
# Sample 1:
# Input
# 1 2 3
# Output
# 1 2 3
# Sample 2:
# Input
# 1 23 456
# Output
# 1 23 456
# Code:
# Replace the underscores with the correct value
# A, B, C = map(int, ______.______)
# print(A, B, C)
#Now write your solution from here:

A, B, C = map(int, input().split())
print(A, B, C)