# Number: 46
# Cost of Groceries
# Jason visited a grocery store for fresh supplies. There are N items in the store where the ith item has a freshness value Ai and cost Bi.
# Jason has decided to purchase all the items having a freshness value greater than equal to X
# Find the total cost of the groceries he buys.
# Input Format
#
#     The first line of input will contain a single integer T, denoting the number of test cases.
#     Each test case consists of multiple lines of input.
#     The first line of each test case contains two space-separated integers N and X — the number of items and the minimum freshness value an item should have.
#     The second line contains N space-separated integers, the array A, denoting the freshness value of each item.
#     The third line contains N space-separated integers, the array B, denoting the cost of each item.
#
# Output Format
# For each test case, output on a new line, the total cost of the groceries Chef buys.
# Constraints
#
#     1≤T≤100
#     1≤N,X≤100
#     1≤Ai,Bi≤100
#
# Sample 1:
# Input
#
# 4
# 2 20
# 15 67
# 10 90
# 3 1
# 1 2 3
# 1 2 3
# 3 100
# 10 90 50
# 30 7 93
# 4 50
# 12 78 50 40
# 40 30 20 10
#
# Output
#
# 90
# 6
# 0
# 50
#
# Explanation:
# Test case 1
# 1: Item 2 has freshness value greater than equal to X=20. Thus, he buys item 2. The total cost is 90.
# Test case 2
# 2: Items 1,2 and 3 have freshness value greater than equal to X=1. Thus, he buys all 3 items. The total cost is 1+2+3=6
# Test case 3
# 3: No item has freshness value greater than equal to X=100. Thus, he buys no items.
# Test case 4
# 4: Items 2 and 3 have freshness value greater than equal to X=50. Thus, he buys items 2 and 3. The total cost is 30+20=50Code:
#
# t = int(input())
#
# while t > 0:
#     n, x = map(int, input().split())
#     a = list(map(int, input().split()))
#     b = list(map(int, input().split()))
#     # Your code goes here

t = int(input())

while t > 0:
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    # Your code goes here
    cost = 0
    for i in range(n):
        if a[i] >= x:
            cost += b[i]

    print(cost)