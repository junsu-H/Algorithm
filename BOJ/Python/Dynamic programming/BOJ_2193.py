# BOJ_2193 이친수

from sys import stdin

input = stdin.readline

def solution():
    n = int(input().rstrip())
    dp = [1] * (n+1)

    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    
    print(dp[n])

solution()