# New Problem Solving:
# Sale Season
# It's the sale season again and Jason bought items worth a total of X dollars. The sale season offer is as follows:
#
#     if X≤100, no discount.
#     if 100<X≤1000, discount is 25 dollars.
#     if 1000<X≤5000, discount is 100 dollars.
#     if X>5000, discount is 500 dollars.
#
# Find the final amount Jason needs to pay for his shopping.
# Input Format
#
#     The first line of input will contain a single integer T, denoting the number of test cases.
#     Each test case consists of single line of input containing an integer X.
#
# Output Format
# For each test case, output on a new line the final amount he needs to pay for his shopping.
# Constraints
#
#     1≤T≤100
#     1≤X≤10000
#
# Sample 1:
# Input
#
# 4
# 15
# 70
# 250
# 1000
#
# Output
#
# 15
# 70
# 225
# 975
#
# Explanation:
# Test case 1
# 1: Since X≤100, there is no discount.
# Test case 3
# 3: Here, X=250. Since 100<250≤1000, discount is of 25 dollars. Therefore, Jason needs to pay 250−25=225 dollars.Code:
#
# T=int(input())
# for i in range(T):
#     X=int(input())

T=int(input())
for i in range(T):
    X=int(input())
    if X<=100:
        print(X)
    elif X <= 1000:
        print(X - 25)
    elif X <= 5000:
        print(X - 100)
    else:
        print(X - 500)
