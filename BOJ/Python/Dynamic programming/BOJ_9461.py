# BOJ_9461 파도반 수열

from sys import stdin

input = stdin.readline

def solution():
    t = int(input().rstrip())

    for _ in range(t):
        dp = [1, 1, 1, 2, 2]

        n = int(input().rstrip())
        
        for i in range(5, n):
            dp.append(dp[i-2] + dp[i-3])

        print(dp[n-1])

solution()