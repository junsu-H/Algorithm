# BOJ_1309 동물원

import sys
sys.setrecursionlimit(10 ** 9)

def solution():
    n = int(sys.stdin.readline().rstrip())
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 3

    for i in range(2, n+1):
        dp[i] = (dp[i-1] + dp[i-1] + dp[i-2]) % 9901

    print(dp[n])

solution()