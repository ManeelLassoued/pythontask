# New Problem Solving:
# Exams
# In Texas, there are X schools, and each school has Y students.
# The year end results are in and a total of Z students passed the exams.
# Assuming that all students appeared for the exams, find whether the number of students who passed in Texas was strictly greater than 50%.
# Input Format
#
#     The first line of input will contain a single integer T, denoting the number of test cases.
#     Each test case consists of three space-separated integers X,Y, and Z, as mentioned in the statement.
#
# Output Format
# For each test case, output on a new line, YES, if the total number of students who passed in Texas was strictly greater than 50%, otherwise print NO.You may print each character of the string in uppercase or lowercase (for example, the strings YES, yEs, yes, and yeS will all be treated as identical).
# Constraints
#
#     1≤T≤2 into 10 to the power 4
#     1≤X≤5
#     1≤Y≤50
#     0≤Z≤X⋅Y
#
# Sample 1:
# Input
#
# 4
# 2 10 12
# 2 10 3
# 1 5 3
# 3 6 9
#
# Output
#
# YES
# NO
# YES
# NO
#
# Explanation:
# Test case 1
# 1: The total number of students appeared were 2⋅10=20. The number of students passed were 12. Thus, number of students who passed are 60%, which is strictly greater than 50%.Test case 2
# 2: The total number of students appeared were 2⋅10=20. The number of students passed were 3.
# Thus, number of students who passed are 15%, which is less than 50%.Test case 3
# 3: The total number of students appeared were 1⋅5=5. The number of students passed were 3.
# Thus, number of students who passed are 60%, which is strictly greater than 50%.Test case 4
# 4: The total number of students appeared were 3⋅6=18. The number of students passed were 9.
# Thus, number of students who passed are 50%, which is equal to 50%.Code:
#
# T=int(input())
# for i in range(T):
#     #your code

T=int(input())
for i in range(T):
    #your code
    a, b, c = map(int, input().split())
    n=a*b
    per = (c/n)*100
    if per>=50:
        print('yes')

    else:
        print('no')
 