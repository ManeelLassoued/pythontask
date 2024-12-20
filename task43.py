# Find maximum in an Array
# Given a list of N integers, representing height of mountains. Find the height of the tallest mountain.
# Input:
#
#     First line will contain T, number of testcases. Then the testcases follow.
#     The first line in each testcase contains one integer, N.
#     The following line contains N space separated integers: the height of each mountains.
#
# Output:
# For each testcase, output one line with one integer: the height of the tallest mountain for that test case.Constraints
#
#     1≤T≤10
#     1≤N≤100000
#     0≤ height of each mountain ≤109
#
# Sample 1:
# Input
#
# 1
# 5
# 4 7 6 3 1
#
# Output
#
# 7
#
# Code:
#
# T=int(input())
# for i in range(T):
#     N=int(input())
#     A=  ___(map(__,input().split()))
#     #your code

T=int(input())
for i in range(T):
    N=int(input())
    A=  list(map(int,input().split()))
    #your code
    k=0
    for j in A:
        if j > k:
            k = j

    print(k)