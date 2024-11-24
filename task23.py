# New Problem Solving:
# Jason has X  5  dollars  and Y 10  dollars. Jason goes to a shop to buy chocolates where each chocolate costs Z
# rupees. Find the maximum number of chocolates that Jason can buy.Input Format
#
#     The first line contains a single integer T — the number of test cases. Then the test cases follow.
#     The first and only line of each test case contains three integers X, Y and Z — the number of 5  dollars, the number of 10  dollars and the cost of each chocolate.
#
# Output Format
# For each test case, output the maximum number of chocolates that Jason can buy.
# Constraints
#
#     1≤T≤100
#     1≤X,Y,Z≤1000
#
# Sample 1:
# Input
#
# 4
# 10 10 10
# 3 1 8
# 8 1 3
# 4 4 1000
#
# Output
#
# 15
# 3
# 16
# 0
#
# Explanation:
# Test case 1
# 1: Jason has 10⋅5+10⋅10=150 dollars in total. Since each chocolate costs 10 dollars, Jason can spend all 150 dollars and buy 15 chocolates.
# Test case 2
# 2: Jason has 3⋅5+1⋅10=25 dollars in total. Since each chocolate costs 8 dollars, Jason can buy a maximum of 3 chocolates, leaving him with 1 dollar.
# Test case 3
# 3: Jason has 8⋅5+1⋅10=50 dollars in total. Since each chocolate costs 3 dollars, Jason can buy a maximum of 16 chocolates, leaving him with 2 dollar.
# Test case 4
# 4: Jason has 4⋅5+4⋅10=60 dollars in total. Since each chocolate costs 1000 dollars, Jason can buy no chocolate, leaving him with 60
# dollars.
# Code:
# t = int(input())
#
# while t > 0:
#     x, y, z = map(int, input().split())
#     # Your code goes here
#     t -= 1


t = int(input())

while t > 0:
    x, y, z = map(int, input().split())
    # Your code goes here
    t -= 1
    if (1 <= x <= 1000) and( 1 <= y <= 1000) and (1 <= z <= 1000):
        q=x*5+y*10
        print(q//z)