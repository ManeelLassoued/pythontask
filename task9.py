#Problem Solving:
# You are given a program which does the following
# Accepts the count of test cases - 't' - in the 1st line.
#         First line of each test case consists of an integer 'N'
#     Outputs the integer which is greater than 'N' by '1'
#
# Sample 1:
# Input
#
# 3
# 1
# 2
# 3
#
# Output
#
# 2
# 3
# 4
#
# Sample 2:
# Input
#
# 3
# 100
# 200
# 300
#
# Output
#
# 101
# 201
# 301
#
# Code:
#
# t = int(input())
# for i in range(t):
#     n = __(input())
#     print(n+__)
#Now write your solution from here:

t = int(input())
for i in range(t):
    n = int(input())
    print(n+1)