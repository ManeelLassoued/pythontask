# New Problem Solving:
# Practice problem - Tax in Texas
# In texas, a tax of dollars 1010 is deducted if the total income is strictly greater than dollars 100.
# Given that total income is X rupees, find out how much money does the Jason take home.
# Input Format
#
#     The first line of input will contain a single integer T, denoting the number of test cases.
#     The first and only line of each test case contains a single integer X — Jason's total income.
#
# Output Format
# For each test case, output on a new line, the amount of money that Chef takes home after deducting tax.
# Sample 1:
# Input
#
# 2
# 101
# 100
#
# Output
#
# 91
# 100
#
# Explanation:
# Test case 1
# 1: Your total income is 101 dollars which is greater than 100 dollars. Thus, a tax of 10 dollars would be deducted and you get 101−10=91
#  dollars.
# Test case 2
# 2: Your total income is 100 dollars which is equal to 100 dollars. Thus, no tax would be deducted and you get 100 dollars.Code:
#
# # Update the code below to solve the problem
#
# t = int(input())
# for i in range(t):
#     X = int(input())

t = int(input())
for i in range(t):
    X = int(input())
    if X>100:
        print(X-10)
    else:
        print(X)
