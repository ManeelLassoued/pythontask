
#Problem Solving:
# Test cases with multiple lines of input
# In the previous problem, we had t test cases and each test case had 1 line of input.
# However, each test case can have multiple lines of input as well.
# We learned how to take multiple inputs in a single line
# Task
# Lets write a program in the IDE which performs the following
#
#     The 1st line of input is an integer t- the count of test cases
#     Each test case consists of 2 lines of input
#     The 1st line of input has 2 space separated integers - accept them as variables A and B
#     The 2nd line of input has 3 space separated integers - accept them as variables C, D and E
#     For each test case - output all integers on a single line
#
# Sample 1:
# Input
#
# 3
# 1 2
# 3 4 5
# 11 22
# 33 44 55
# 1 23
# 456 789 101112
#
# Output
#
# 1 2 3 4 5
# 11 22 33 44 55
# 1 23 456 789 101112
#
# Explanation:
# 2 lines of input in test case 1:
# 1 2
# 3 4 5
# Output 1: 1 2 3 4 52 lines of input in test case 2:
# 11 22
# 33 44 55
# Output 2: 11 22 33 44 552 lines of input in test case 3:
# 1 23
# 456 789 101112
# Output 3: 1 23 456 789 101112Code:
#
# t = int(input())
#
# for i in range(_):

    # accept 2 integers on the 1st line using map


    # accept 3 integers on the 2nd line using map


    # output the 5 integers on a single line for each test case
# print(A, B, C, D, E)
#Now write your solution from here:


t = int(input())

for i in range(t):
    # accept 2 integers on the 1st line using map
    A, B =  map(int, input().split())
    # accept 3 integers on the 2nd line using map
    C, D, E =  map(int, input().split())

    # output the 5 integers on a single line for each test case
    print(A, B, C, D, E)