# Problem Solving:
# How to accept multiple integers on separate lines
# Let's make this a little bit more complicated.You need to write a program which does the following
# Accepts 2 integers as input in 1st line as the variables A, B
# Accepts 3 integers as input in the 2nd line as the variables C, D and E
# Accepts 4 integers as input in the 3rd line as the variables F, G, H and I
# Prints out 9 integers as output in a single line to the console
# Sample 1:
# Input
# 1 2
# 3 4 5
# 6 7 8 9
# Output
# 1 2 3 4 5 6 7 8 9
# Sample 2:
# Input
# 12 34
# 567 789 101112
# 13 14 15 16
# Output
# 12 34 567 789 101112 13 14 15 16
# Code:
# Update the '_' in the code belowA, B = map(___,___)
# C, D, E = map(int, input().split())
# F, G, H, I = ___(int,input()._______)
# _____(A, B, C, D, E, F, G, H, I)
#Now write your solution from here:

A, B = map(int,input().split())
C, D, E = map(int, input().split())
F, G, H, I = map(int,input().split())
print(A, B, C, D, E, F, G, H, I)