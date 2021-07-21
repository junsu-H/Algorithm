# BOJ_1003 피보나치 함수

from sys import stdin

input = stdin.readline

def solution():
    t = int(input().rstrip())
    dp = [[0, 0]] * 41
    dp[0] = [1, 0]
    dp[1] = [0, 1]
    for i in range(t):
        n = int(input().rstrip())
        
        if n == 0:
            print(' '.join(map(str, dp[0])))
        elif n == 1:
            print(' '.join(map(str, dp[1])))
        else:
            for i in range(2, n+1):
                dp[i] = [dp[i-1][1], dp[i-1][0] + dp[i-1][1]]
            print(' '.join(map(str, dp[n])))

solution()