# New Problem Solving:Review syntax usage
# Let us cover the 'conditional statements' syntax required for solving beginner's programming problems.Task
# Write a program which does the following
#     Accepts the count of test cases - t
#      -> Each test case has one integer N
#     Output the following for each test case
#     -> If input is less than or equal to 100, output 'Good'
#     -> If input is greater than 100 but less than or equal to 200, output 'Better'
#     ->If the input is greater than 200, output 'Best'
# Sample 1:
# Input
# 3
# 100
# 200
# 201
# Output
# Good
# Better
# Best
# Code:
# # Update the blanks in the code below
# t = int(input())
# for i in range(t):
#     #Accept 1 integer as input.
#     N = int(___)
#     #1st condition in the problem
#     if N__100:
#         print('Good')
#     #2nd condition in the problem
#     elif N__100 and N__200:
#         print('Better')
#     #3rd condition in the problem
#     else:
#         print('Best')

# # Update the blanks in the code below

t = int(input())
for i in range(t):
    #Accept 1 integer as input.
    N = int(input())
    #1st condition in the problem
    if N<=100:
        print('Good')
    #2nd condition in the problem
    elif N>100 and N<=200:
        print('Better')
    #3rd condition in the problem
    else:
        print('Best')