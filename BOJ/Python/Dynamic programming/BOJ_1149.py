# BOJ_1149 RGB 거리

from sys import stdin

input = stdin.readline

def solution():
    n = int(input().rstrip())
    home = [list(map(int, input().rstrip().split())) for _ in range(n)]

    for i in range(1, n):

        home[i][0] += min(home[i-1][1], home[i-1][2])
        home[i][1] += min(home[i-1][0], home[i-1][2])
        home[i][2] += min(home[i-1][0], home[i-1][1])

    print(min(home[n-1]))

solution()