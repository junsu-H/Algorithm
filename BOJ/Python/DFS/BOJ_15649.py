# BOJ_15649 N과 M (1)

from sys import setrecursionlimit

setrecursionlimit(10**5)

def dfs(level):
    if level == M:
        print(*answer)

    else:
        for i in range(1, N+1):
            if check[i] == 0:
                check[i] = 1
                answer[level] = i
                dfs(level + 1)
                check[i] = 0

N, M = map(int, input().split())
answer = [0] * M
check = [0] * (N+1)
count = 0
dfs(0)