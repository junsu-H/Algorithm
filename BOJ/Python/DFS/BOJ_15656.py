# BOJ_15656 N과 M (7)

from sys import setrecursionlimit

setrecursionlimit(10**5)

def dfs(level):
  if level == M:
    print(*answer)

  else:
    for i in range(1, N+1):
        visit[i] = 1
        answer[level] = data[i]
        dfs(level+1)
        visit[i] = 0

N, M = map(int, input().split())
data = [0] + sorted(list(map(int, input().split())))

answer = [0] * M
visit = [0] * (N+1)

dfs(0)