# Problem Solving:
# String mirror - Double strings
# Write a program in the IDE which does the following
# Accepts the count of test cases  t in the 1st line
# First line of each test case consists of a string S
# You need to perform the following operation
# Create a variable X which contains the string S concatenated with the string S
# Output X for each test case
# Sample 1:
# Input
# 3
# ab
# bc
# cd

# Output
# abab
# bcbc
# cdcd

# Code:
# t = int(input())
# for i in range(t):
#     # take input and output the join using +

#Now write your solution from here:
t = int(input())
for i in range(t):
    S= input()
    X = S + S
    print(X)