# New Problem Solving:
# Search an element in an array
# You are given an array A of size N and an element X. Your task is to find whether the array A contains the element X or not.Input Format
#
#     The first line contains two space-separated integers N and X — the size of array and the element to be searched.
#     The second line contains all the elements of array A
#
# Output Format
# Output "YES" if the element X is present in A, otherwise output "NO".
# Constraints
#
#     1≤N≤10 to the power of 5
#     1≤Ai≤10 to the power 5
#
# Sample 1:
# Input
#
# 5 3
# 7 3 5 2 1
#
# Output
#
# YES
#
# Sample 2:
# Input
#
# 5 10
# 7 3 5 2 1
#
# Output
#
# NO
#
# Code:
#
# N, X = map(int, input().split())
#
# A = list(map(int, input().split()))
#

N, X = map(int, input().split())

A = list(map(int, input().split()))
m=0
#your code
for i in range(N):
    if A[i] ==  X :
      m= A[i]

if m == 0:
    print('no')
else:
    print('yes')

