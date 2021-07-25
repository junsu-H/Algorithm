# BOJ_11727 2xn 타일링 2

from sys import stdin

input = stdin.readline

def solution():
    n = int(input().rstrip())
    dp = [0, 1, 3, 5, 11]

    for i in range(5, n+1):
        dp.append((dp[i-1] + dp[i-2] * 2)  % 10007)

    print(dp[n])

solution()