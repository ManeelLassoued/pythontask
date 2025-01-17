# Number:49
# Different Consecutive Characters
# Jason has a binary string S of length N. Jason can perform the following operation on S:
#
#     Insert any character (0 or 1) at any position in S.
#
# Find the minimum number of operations Jason needs to perform so that no two consecutive characters are same in S.
# Input Format
#
#     The first line contains a single integer T — the number of test cases. Then the test cases follow.
#     The first line of each test case contains an integer N — the length of the binary string S.
#     The second line of each test case contains a binary string S of length N containing 0s and 1s only.
#
# Output Format
# For each test case, output on a new line the minimum number of operations Jason needs to perform so that no two consecutive characters are same in S.
# Constraints
#
#     1≤T≤100
#     1≤N≤1000
#
# Sample 1:
# Input
#
# 3
# 2
# 11
# 4
# 0101
# 5
# 00100
#
# Output
#
# 1
# 0
# 2
#
# Explanation:
# Test case 1: We can perform the following operations: 11→1‾1
# It should be 10 or 01 so,11→1 operation
# Test case 2: We do not need to perform any operations.
# Test case 3: We can perform the following operations: 00100→0‾010‾0
# It should be 10101 or 01010. so, 00100→2 operations
# Code:

T=int(input())
for i in range(T):
    N=int(input())
    S=input()
    #write your code
    count=0
    for j in range(len(S) - 1):
         if S[j]==S[j+1]:
             count+=1
         else:
            count+=0
    print(count)


