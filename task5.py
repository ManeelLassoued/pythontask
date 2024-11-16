#Problem Solving:
# How to accept string inputs
# Lets try the same exercise with strings.Remember that the input() function takes the parameters as strings and then we convert to integer as needed. We use map function convert input to integers. Here we just want to take input as string, so no need of map.
# a, b = input().split()
# print(a, b)
# Task
# You need to write a program which does the following
#
#     Accepts 2 space separated alphanumeric strings as input in 1st line as the variables A, B
#     Accepts 3 space separated alphanumeric strings as input in 2nd line as the variables C, D, E
#     Accepts 4 space separated alphanumeric strings as input in 3rd line as the variables F, G, H, I
#     Prints out 9 space separated strings as output in a single line to the console
#
# Sample 1:
# Input
#
# abc cde
# fg hi jk
# l m n o
#
# Output
#
# abc cde fg hi jk l m n o
#
# Code:
# # # Update the '_' in the code belowA, B = input()._____
# C, D, E = input().split()
# F, G, H, I = input()._____
#  _____(A, B, C, D, E, F, G, H, I)
#Now write your solution from here:

A, B = input().split()
C, D, E = input().split()
F, G, H, I = input().split()
print(A, B, C, D, E, F, G, H, I)