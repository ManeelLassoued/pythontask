# Problem Solving:
# Basic math - Addition and multiplication
# Basic math and logic based programming problems are the correct starting point for Beginners.
#     In the previous module, we have learnt how to accept multiple inputs and test cases
#     The current module will use our knowledge of python syntax and learnings from the previous module
#
# Task
# Lets start with a simple problem - you need to write a program which does the following
#
#     Accepts the number of inputs / test cases as t The only line of each test case contains 2 integers - declare them as variables A and B
#     For each test case, you need to perform the following operations
#     Create a variable - S the sum of the 2 input integers
#     Create a variable - P the product of the 2 input integers
#     Output 2 space separated integers - S and P in a single line
#
# Note:
#
#     The syntax for product of 2 integers in Python is (X * Y)
#
# Sample 1:
# Input
#
# 2
# 5 10
# 3 4
#
# Output
#
# 15 50
# 7 12
#
# Explanation:
# Test case 1:
# The 2 integers are 5 and 10
# and we output 15as their sum and 50
# as their productTest case 2: The 2 integers are 3 and 4
#  we output 7 and 12  as their sum and product respectively
# code:
#
# # Update the '_' in the code below
#
# t = int(input())
# for i in range(t):
#     #Accept 2 integers inputs
#     A, B = map(___,___)
#     #Sum of inputs
#     S = A _ B
#     #Product of inputs
#     P = A _ B
#     #Print the desired output for each test case
#     print(_,_)
#Now write your solution from here:

# Update the '_' in the code below

t = int(input())
for i in range(t):
    #Accept 2 integers inputs
    A, B = map(int,input().split())
    #Sum of inputs
    S = A + B
    #Product of inputs
    P = A * B
    #Print the desired output for each test case
    print(S,P)

