# BOJ_9095 1,2,3 더하기

import sys

sys.setrecursionlimit(10 ** 9)

def solution():
    dp = [0] * 12
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4

    t = int(sys.stdin.readline().rstrip())

    for _ in range(t):
        n = int(sys.stdin.readline().rstrip())
        for i in range(4, n+1):
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
        print(dp[n])

solution()