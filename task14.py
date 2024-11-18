#New Problem Solving:
#Practice problem - Tuition fees
#Let's solve this practice problem.
#You will attend tuitions for X
#X weeks, and the cost of tuition per week is Y dollars.
# You need to compute and output your total tuition fees.
# Hint
#     Refer to the multiplication syntax you learnt in the previous questions
#     Run your code on the sample test cases before submitting the same
# Input Format
#     The first line of input will contain an integer T— the number of test cases.
#     The first and only line of each test case contains two space-separated integers X and Y
# Output Format
#     For each test case, output on a new line your total tuition fees.
# Sample 1:
# Input
# 4
# 1 10
# 1 15
# 2 10
# 2 15

# Output:
# 10
# 15
# 20
# 30

# Code:

# Update the code below to solve the problem
# t = int(input())
# for i in range(t):
#     X, Y = map(int, input().split())
#Now write your solution from here:

t = int(input())
for i in range(t):
    X, Y = map(int, input().split())
    print( X * Y)