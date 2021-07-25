# BOJ_11726 2xn 타일링

from sys import stdin

input = stdin.readline

def solution():
    n = int(input().rstrip())
    dp = [0, 1, 2, 3]

    for i in range(4, n+1):
        dp.append((dp[i-1] + dp[i-2]) % 10007)

    print(dp[n])

solution()