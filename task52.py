# Number 52:
# World Chess Championship
# The World Chess Championship 2022 is about to start. 14 Classical games will be played between Jason and Carlsen in the championship, where each game has one of three outcomes — it can be won by Carlsen, won by Jason, or it can be a draw. The winner of a game gets 2 points, and the loser gets 0 points. If it’s a draw, both players get 1 point each.
# The total prize pool of the championship is 100⋅X. At end of the 14 Classical games, if one player has strictly more points than the other, he is declared the champion and gets 60⋅X as his prize money, and the loser gets 40⋅X.
# If the total points are tied, then the defending champion Carlsen is declared the winner. However, if this happens, the winner gets only 55⋅X, and the loser gets 45⋅X.
# Given the results of all the 14 games, output the prize money that Carlsen receives.
# The results are given as a string of length 14 consisting of the characters C, N, and D.
#
#     C denotes a victory by Carlsen.
#     N denotes a victory by Jason.
#     D denotes a draw.
#
# Input Format
#
#     The first line of input contains an integer T, denoting the number of test cases. The description of T test cases follows.
#     The first line of each test case contains one integer X, denoting that the total prize pool is 100⋅X.
#     The second line contains the results of the match, as a string of length 14 containing only the characters C, N, and D.
#
# Output Format
# For each test case, output in a single line the total prize money won by Carlsen.
# Constraints
#
#     1≤T≤1000
#     1≤X≤10 to the power 6
#     ∣S∣=14
#     S contains only characters D, C, N.
#
# Subtasks
# Subtask #1 (100 points): Original constraints
# Sample 1:
# Input
#
# 4
# 100
# CCCCCCCCCCCCCC
# 400
# CDCDCDCDCDCDCD
# 30
# DDCCNNDDDCCNND
# 1
# NNDNNDDDNNDNDN
#
# Output
#
# 6000
# 24000
# 1650
# 40
#
# Explanation:
# Test case 1
# 1: Since Carlsen won all the games, he will be crowned the champion and will get 60⋅X as the prize money which is 60⋅100=6000
# Test case 2
# 2: Carlsen won 7 games and drew 7, so his score is 2⋅7+1⋅7=21. Jason lost 7 games and drew 7, so his score is 0⋅7+1⋅7=7. Since Carlsen has more points, he will be crowned the champion and will get 60⋅X as the prize money which is 60⋅400=24000
# Test case 3
# 3: Carlsen and Jason both end up with 14 points. So, Carlsen is declared the winner, but because the points were tied, he receives 55⋅X=55⋅30=1650 in prize money.Code:

T=int(input())
for _ in range(T):
    X=int(input())
    S=input()
    #write your code
    c=0
    d=0
    n=0
    for j in range(len(S)):
        if S[j]=='C':
           c+=1
        elif S[j]=='D':
            d+=1
        elif S[j]=='N':
             n+=1
        else:
            exit()

    if c*2+d*1 > n*2+d*1  :
        print(X * 60)
    elif   c*2+d*1 < n*2+d*1:
        print(X * 40)
    else:
        print(X * 55)



