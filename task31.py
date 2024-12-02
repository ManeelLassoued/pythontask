# New Problem Solving:
# Subscriptions
# A new TV streaming service was recently started in Texas called the Texas-TV.
# A group of N friends in Texas want to buy Texas-TV subscriptions. We know that 6 people can share one Texas-TV subscription. Also, the cost of one Texas-TV subscription is X dollars. Determine the minimum total cost that the group of N friends will incur so that everyone in the group is able to use Texas-TV.
# Input Format
#
#     The first line contains a single integer T— the number of test cases. Then the test cases follow.
#     The first and only line of each test case contains two integers N and X — the size of the group of friends and the cost of one subscription.
#
# Output Format
# For each test case, output the minimum total cost that the group will incur so that everyone in the group is able to use Texas-TV.
# Constraints
#
#     1≤T≤1000
#     1≤N≤100
#     1≤X≤1000
#
# Sample 1:
# Input
#
# 3
# 1 100
# 12 250
# 16 135
#
# Output
#
# 100
# 500
# 405
#
# Explanation:
#
#     Test case 1: There is only one person in the group. Therefore he will have to buy 1 subscription. Therefore the total cost incurred is 100
#     Test case 2: There are 12 people in the group. Therefore they will have to buy 2 subscriptions. Therefore the total cost incurred is 500
#     Test case 3: There are 16 people in the group. Therefore they will have to buy 3 subscriptions. Therefore the total cost incurred is 405.
#
# Code:
#
# #your code
import math

T=int(input())
for i in range(T):
    #your code
    n, x = map(int, input().split())
    if(n > 6):
        div= math.ceil(n / 6)
        print( div *x)
    else:
        print(x)
