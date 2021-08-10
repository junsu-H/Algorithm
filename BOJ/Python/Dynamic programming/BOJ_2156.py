# BOJ_2156 포도주 시식

from sys import stdin

input = stdin.readline

def solution():
    n = int(input().rstrip())
    wine = [int(input().rstrip()) for _ in range(n)]
    wine.insert(0, 0)
    dp = [0, wine[1]]

    if n > 1:
        dp.append(wine[1] + wine[2])

    for i in range(3, n + 1):
        dp.append(max(dp[i-1], dp[i-3] + wine[i-1] + wine[i], dp[i-2] + wine[i]))
    print(dp[n])

solution()