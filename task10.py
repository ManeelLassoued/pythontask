t = int(input())

for i in range(t):
    # accept 2 integers on the 1st line of each test case
    A, B = map(int,input().split())

    # accept 1 string on the 2nd line of each test case
    C = input()

    # output the 2 integers and 1 string on a single line
    print(A, B, C)