# New Problem solving:
# Scalene Triangle
# Given A,B, and C as the sides of a triangle, find whether the triangle is scalene.Note:
#
#     A triangle is said to be scalene if all three sides of the triangle are distinct.
#     It is guaranteed that the sides represent a valid triangle.
#
# Input Format
#
#     The first line of input will contain a single integer T, denoting the number of test cases.
#     Each test case consists of three space-separated integers A,B, and C — the length of the three sides of the triangle.
#
# Output Format
# For each test case, output on a new line, YES, if the triangle is scalene, and NO otherwise.
# You may print each character of the string in uppercase or lowercase. For example, YES, yes, Yes, and yEs are all considered identical.Constraints
#
#     1≤T≤100
#     1≤A≤B≤C≤10
#     C<(A+B)
#
# Sample 1:
# Input
#
# 4
# 2 3 4
# 1 2 2
# 2 2 2
# 3 5 6
#
# Output
#
# YES
# NO
# NO
# YES
#
# Explanation:
# Test case 1
# 1: The side lengths are 2,3, and 4 Since no two side lengths are equal, the triangle is scalene.
# Test case 2
# 2: The side lengths are 1,2, and 2. The sides B and C have the same length. Thus, the triangle is not scalene.
# Test case 3
# 3: The side lengths are 2,2, and 2. The sides A,B, and C have the same length. Thus, the triangle is not scalene.
# Test case 4
# 4: The side lengths are 3,5, and 6. Since no two side lengths are equal, the triangle is scalene.Code:

# t = int(input())

# while t > 0:
#     a, b, c = map(int, input().split())
#     # Your code goes here
#     t -= 1


t = int(input())

while t > 0:
    a, b, c = map(int, input().split())
    # Your code goes here
    t -= 1
    if c < (a+b) and (a !=b !=c):
        print('YES')
    else:
        print('NO')