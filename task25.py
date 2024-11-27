# New Problem Solving:
# Candy Store
# Jason has started working at the candy store. The store has 100 chocolates in total.
# Jason’s daily goal is to sell X chocolates. For each chocolate sold, he will get 1 dollar. However, if Jason exceeds his daily goal, he gets 2
# dollars per chocolate for each extra chocolate.
# If he sells Y chocolates in a day, find the total amount he made.
# Input Format
#
#     The first line of input will contain a single integer T, denoting the number of test cases.
#     Each test case consists of two space-separated integers X  and Y the daily goal of him, and the number of chocolates he actually sells.
#
# Output Format
# For each test case, output on a new line the total amount Jason made in a day.
# Constraints
#
#     1≤T≤100
#     1≤X,Y≤10
#
# Sample 1:
# Input
#
# 4
# 3 1
# 5 5
# 4 7
# 2 3
#
# Output
#
# 1
# 5
# 10
# 4
#
# Explanation:
# Test case 1
# 1: Jaon's daily goal was 3 since he sold only 1 chocolate, he'll get only 1 dollar.
# Test case 2
# 2: Jason's daily goal was 5 Since he sold 5 chocolates, he'll get 5 dollars.
# Test case 3
# 3: Jason's daily goal was 4 Since he sold 7 dollar, he'll get 4 dollars for the 4 chocolates as his daily goal and 2 dollars per chocolate for the extra 3 chocolates. The total amount he gets is 4+3⋅2=10
# Test case 4
# 4: Jason's daily goal was 2 Since he sold 3 chocolate, he'll get 2 dollars for the 2 chocolates as his daily goal and 2 dollars per chocolate for the extra 1 chocolate. The total amount he gets is 2+1⋅2=4Code:
#
# # t = int(input())
#
# # while t > 0:
# #     x, y = map(int, input().split())
# #     # Your code goes here
# #     t -= 1

t = int(input())

while t > 0:
    x, y = map(int, input().split())
    # Your code goes here
    t -= 1
    if y>x:
     extra  =  y -x
     print(x+ extra * 2 )
    else:
        print(y)
