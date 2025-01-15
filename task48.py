# Number 48:
# Running Comparison
# Alice and Bob recently got into running, and decided to compare how much they ran on different days.
# They each ran for N days — on the ith day, Alice ran Ai meters and Bob ran Bi meters.
# On each day,
#
#     Alice is unhappy if Bob ran strictly more than twice her distance, and happy otherwise.
#     Similarly, Bob is unhappy if Alice ran strictly more than twice his distance, and happy otherwise.
#
# For example, on a given day
#
#     If Alice ran 200 meters and Bob ran 500, Alice would be unhappy but Bob would be happy.
#     If Alice ran 500 meters and Bob ran 240, Alice would be happy and Bob would be unhappy.
#     If Alice ran 300 meters and Bob ran 500, both Alice and Bob would be happy.
#
# On how many of the N days were both Alice and Bob happy?
# Input Format
#
#     The first line of input will contain a single integer T, denoting the number of test cases.
#     Each test case consists of three lines of input.
#     The first line of each test case contains a single integer N— the number of days.
#     The second line of each test case contains N space-separated integers A1,A2,…,AN — the distances run by Alice on the N days.
#     The third line of each test case contains N space-separated integers B1,B2,…,BN — the distances run by Bob on the N days.
#
# Output Format
# For each test case, output on a new line the number of days when both Alice and Bob were happy.
# Constraints
#
#     1≤T≤1000
#     1≤N≤100
#     1≤Ai,Bi≤105
#
# Sample 1:
# Input
#
# 4
# 3
# 100 200 300
# 300 200 100
# 4
# 1000 1000 1000 1000
# 400 500 600 1200
# 4
# 800 399 1400 532
# 2053 2300 3400 23
# 5
# 800 850 900 950 1000
# 600 800 1000 1200 1400
#
# Output
#
# 1
# 3
# 0
# 5
#
# Explanation:
# Test case 1
# 1: Alice is unhappy on the first day, since she ran 100 meters but Bob ran 300; and 300 is more than twice of 100.
# Similarly, Bob is unhappy on the third day.
# Both Alice and Bob are happy on the second day, so the answer is 1.
# Test case 2
# 2: Bob is unhappy on day 1 and happy on every other day, while Alice is happy on every day. So, they're both happy on three days — the second, third, and fourth.
# Test case 3
# 3: Alice is unhappy on days 1,2,3 and Bob is unhappy on day 4.
# Test case 4
# 4: Alice and Bob are both happy on all five days.
# Code:

t = int(input())

while t > 0:
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    t -= 1
    # Your code goes here
    count=0
    for i in range(n):
          if a[i] <= b[i] and (b[i]/2<= a[i]):
              count +=1
          elif a[i] >= b[i] and (a[i]/2<= b[i]):
              count +=1
          else:
              count +=0

    print(count)



