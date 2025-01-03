# New Problem Solving:
# Water Filling
# Jason has three water bottles. At any point, if at least two of them are empty, she will fill them up. But if at most one bottle is empty, he will wait, and not fill them up now.
# You are given three integers - B1,B2, and B3.
# If B1=1, it means that the first bottle is full.
# If B1=0, it means that the first bottle is empty.
# Similarly, B2 denotes whether the second bottle is full or empty, and B3 denotes it for the third bottle.
# Output "Water filling time", if Jason has to fill the bottles now. If not, output "Not now".
# Input Format
#
#     The first line of input will contain a single integer T, denoting the number of test cases.
#     The only line of each test case contains three space-separated integers, B1,B2,B3
#
# Output Format
# For each test case, output on a new line, either "Water filling time", or "Not now".
# Constraints
#
#     1≤T≤1000
#     Bi is either 0 or 1
#
# Sample 1:
# Input
#
# 5
# 0 0 0
# 1 1 1
# 1 1 0
# 0 1 0
# 0 1 1
#
# Output
#
# Water filling time
# Not now
# Not now
# Water filling time
# Not now
#
# Explanation:
# Testcase 1: The inputs are 0,0,0. So all three bottles are empty. Since at least two bottles are empty, it is "Water filling time".
# Testcase 2: The inputs are 1,1,1. So all three bottles are full. Since it is not the case that at least two bottles are empty, it is "Not now".
# Testcase 3: The inputs are 1,1,0. So only one bottle is empty. Since it is not the case that at least two bottles are empty, it is "Not now".
# Testcase 4: The inputs are 0,1,0. So two bottles are empty. Since at least two bottles are empty, it is "Water filling time".
# Testcase 5: The inputs are 0,1,1. So only one bottle is empty. Since it is not the case that at least two bottles are empty, it is "Not now".Code:
#
# T=int(input())
# for i in range(T):
#     B1,B2,B3=map(int,input().split())
#     #your code
T=int(input())
for i in range(T):
    B1,B2,B3=map(int,input().split())
    #your code
    if B1 > 1 or  B2 > 1 or  B3 > 1:
        print("")
    else:
        if B1 == 1 and B2 == 1 and B3 == 1:
         print("Not now")
        elif B1 == 1 and  B2 == 1 and B3 == 0:
         print("Not now")
        elif B1 == 1 and B2 == 0 and B3 == 1:
         print("Not now")
        elif B1 == 0 and  B2 == 1 and B3 == 1:
         print("Not now")
        elif B1 == 0 and  B2== 0 and B3 == 0:
          print("Water filling time")
        elif B1 == 1 and  B2 == 0 and B3 == 0:
          print("Water filling time")
        elif B1 == 0 and  B2 == 1 and B3 == 0:
                print("Water filling time")
        else:
            print("Water filling time")



