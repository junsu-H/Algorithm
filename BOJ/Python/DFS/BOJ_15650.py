# BOJ_15650 N과 M (2)

from sys import setrecursionlimit

setrecursionlimit(10**5)

def dfs(level, number):
    if level == M:
        print(*answer)
    
    else:
        for i in range(number, N+1):
            answer[level] = i
            dfs(level + 1, i + 1)

N, M = map(int, input().split())
answer = [0] * M
check = [0] * (N+1)
count = 0
dfs(0, 1)