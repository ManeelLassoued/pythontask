# New Problem Solving:
# Second Max of Three Numbers
# Problem Statement
# Write a program that accepts sets of three numbers, and prints the second-maximum number among the three.Input
#     First line contains the number of triples, N.
#     The next N lines which follow each have three space separated integers.
#
# Output
# For each of the N triples, output one new line which contains the second-maximum integer among the three.Constraints
#
#     1 ≤ N ≤ 6
#     1 ≤ every integer ≤ 10000
#     The three integers in a single triplet are all distinct. That is, no two of them are equal.
#
# Sample 1:
# Input
#
# 3
# 1 2 3
# 10 15 5
# 100 999 500
#
# Output
#
# 2
# 10
# 500
#
# Code:
# #your code
N = int(input())
if N>=1 or N<=6:
 for i in range(N):
    a,b,c =map(int,input().split())
    if a<b and a>c:
        print(a)
    elif b>a and b<c:
        print(b)
    else:
        print(c)


