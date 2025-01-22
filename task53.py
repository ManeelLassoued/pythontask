# Number 53:
# Jason and Happy String
# Jason has a string S with him. Jason is happy if the string contains a contiguous substring of length strictly greater than 2 in which all its characters are vowels.
# Determine whether Jason is happy or not.
# Note that, in english alphabet, vowels are a, e, i, o, and u.
# Input Format
#
#     First line will contain T, number of test cases. Then the test cases follow.
#     Each test case contains of a single line of input, a string S.
#
# Output Format
# For each test case, if Jason is happy, print HAPPY else print SAD.
# You may print each character of the string in uppercase or lowercase (for example, the strings hAppY, Happy, haPpY, and HAPPY will all be treated as identical).
# Constraints
#
#     1≤T≤1000
#     3≤∣S∣≤1000, where ∣S∣ is the length of S.
#     S will only contain lowercase English letters.
#
# Sample 1:
# Input
#
# 4
# aeiou
# abxy
# aebcdefghij
# abcdeeafg
#
# Output
#
# Happy
# Sad
# Sad
# Happy
#
# Explanation:
# Test case 1
# 1: Since the string aeiou is a contiguous substring and consists of all vowels and has a length >2, Jason is happy.
# Test case 2
# 2: Since none of the contiguous substrings of the string consist of all vowels and have a length >2, Jason is sad.
# Test case 3
# 3: Since none of the contiguous substrings of the string consist of all vowels and have a length >2, Jason is sad.
# Test case 4
# 4: Since the string eea is a contiguous substring and consists of all vowels and has a length >2, Jason is happy.Code:

t = int(input())

while t > 0:
    s = input()
    # Your code goes here
    t -= 1
    main_string='aeiou'
    count=0
    #write your code
    k=""

    for j in range(len(s)):
        if s[j] in{'a','e','i','o','u'} :
            count += 1
            k+=s[j]
        elif  s[j] not in{'a','e','i','o','u'} and count<2:
            k = ""
            count=0
        elif s[j] not in {'a', 'e', 'i', 'o', 'u'} and count > 2:
            break
    if count >2 and k in s  :
        print("HAPPY")

    else:
        print("SAD")




