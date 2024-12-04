# New Problem Solving:CRED Coins
# For each bill you pay using CRED, you earn X CRED coins.
# At store, each bag is worth 100 CRED coins.
# Jason pays Y number of bills using CRED. Find the maximum number of bags he can get from the store.
# Input Format
#
#     First line will contain T, number of test cases. Then the test cases follow.
#     Each test case contains of a single line of input, two integers X and Y.
#
# Output Format
# For each test case, output in a single line - the maximum number of bags he can get from the  store.
# Constraints
#
#     1≤T≤100
#     1≤X,Y≤1000
#
# Subtasks
#
#     Subtask 1 (100 points): Original constraints.
#
# Sample 1:
# Input
#
# 3
# 10 10
# 20 4
# 70 7
#
# Output
#
# 1
# 0
# 4
#
# Explanation:
# Test Case 1
# 1: For each bill payment, one receives 10 CRED coins. Jason pays 10 bills using CRED. Thus, he receives 100 CRED coins. Jason can get 1
#  bag from the  store using these coins.
# Test Case 2
# 2: For each bill payment, one receives 20 CRED coins. Jason pays 4 bills using CRED. Thus, he receives 80 CRED coins. Jason cannot get any bag from the  store using these coins.
# Test Case 3
# 3: For each bill payment, one receives 70 CRED coins. Jason pays 7 bills using CRED. Thus, he receives 490 CRED coins. Jason can get at most 4 bags from the store using these coins.Code:
#
# T=int(input())
# for i in range(T):
#     X,Y=map(int,input().split())
#     #your code

T=int(input())
for i in range(T):
    X,Y=map(int,input().split())
    #your code
    CRED = X * Y
    print(CRED//100)