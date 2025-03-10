# New Problem Solving:
# Fitness
# Jason wants to become fit for which he decided to walk to the office and return home by walking.
# It is known that Jason's office is X km away from his home.
# If his office is open on 5 days in a week,
# find the number of kilometers Chef travels through office trips in a week.
# Input Format
#     First line will contain T, number of test cases. Then the test cases follow.
#     Each test case contains of a single line consisting of single integer X.
# Output Format
# For each test case, output the number of kilometers Chef travels through office trips in a week.
# Constraints
#     1≤T≤10
#     1≤X≤10
# Sample 1:
# Input
# 4
# 1
# 3
# 7
# 10
#
# Output
# 10
# 30
# 70
# 100
#
# Explanation:
# Test case 1
# 1: The office is 1 km away. Thus, to go to the office and come back home, Jason has to walk 2 kms in a day. In a week with 5 working days, Jason has to travel 2⋅5=10 kms in total.
# Test case 2
# 2: The office is 3 kms away. Thus, to go to the office and come back home, Jason has to walk 6 kms in a day. In a week with 5  working days, Jason has to travel 6⋅5=30 kms in total.
# Test case 3
# 3: The office is 7 kms away. Thus, to go to the office and come back home, Jason has to walk 14 kms in a day. In a week with 5 working days, Jason has to travel 14⋅5=70 kms in total.
# Test case 4
# 4: The office is 10 kms away. Thus, to go to the office and come back home, Jason has to walk 20 kms in a day. In a week with 5 working days, Jason has to travel 20⋅5=100 kms in total.
# t = int(input())
#
# while t > 0:
#     x = int(input())
#     t -= 1
#     # Your code goes here

t = int(input())

while t > 0:
    x = int(input())
    t -= 1
    # Your code goes here
    if   x > 10 or x < 1 or t > 10 or t < 0:
        exit()

    else:
        print(x * 10)



