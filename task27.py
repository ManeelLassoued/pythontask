# New Problem solving:
# Sum of Digits
# You're given an integer N. Write a program to calculate the sum of all the digits of N.Input Format
# The first line contains an integer T, the total number of testcases. Then follow T lines, each line contains an integer N.
# Output Format
# For each test case, calculate the sum of digits of N, and display it in a new line.
# Constraints
#
#     1≤T≤1000
#     1≤N≤1000000
#
# Sample 1:
# Input
#
# 3
# 12345
# 31203
# 2123
#
# Output
#
# 15
# 9
# 8
#
# Code:
#your code
t = int(input())

while t > 0:

   N = int(input())
   t -= 1
   s=str(N)
   sum=0
   for i in  s :
       sum  =int(i)+sum

   print(sum)



