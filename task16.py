# New Problem Solving:
# Debug this code - Total prize money
# The code given in the IDE is incorrect - Try and debug this program!!!In a coding contest, there are prizes for the top rankers. The prize scheme is as follows:
#     Top 10 participants receive dollars X each.
#     Participants with rank 11to 100 (both inclusive) receive dollars Y each.
# Find the total prize money over all the participants.
# Input Format
#
#     First line will contain T, number of test cases. Then the test cases follow.
#     Each test case contains of a single line of input, two integers X and Y - the prize for top 10 rankers and the prize for ranks 11 to 100 respectively.
#
# Output Format
# For each test case, output the total prize money over all the contestants.
# Sample 1:
# Input
# 2
# 80 1
# 400 30
# Output
# 890
# 6700

# Explanation:
# Test Case 1
# 1: Top 10 participants receive rupees 80 and next 90 participants receive dollar 1each. So, total prize money =10⋅80+90⋅1=890
# Test Case 2
# 2: Top 10 participants receive rupees 400 and next 90 participants receive rupees 30 each. So, total prize money =10⋅400+90⋅30=6700
# Code:
#
# # The code
#
# # The code below is incorrect. Debug this code to solve the problem.
#
# t = int(input())
# for i in range(t):
#     X, Y = map(int, input().split())
#     prize_top10 = 10 * X
#     prize_11to100 = 100 * Y
#     print(prize_top10 + prize_11to100)

#Now write your solution from here:
t = int(input())
for i in range(t):
    X, Y = map(int, input().split())
    prize_top10 =  (10*X)
    prize_11to100 = (90*Y)
    print(prize_top10 + prize_11to100)