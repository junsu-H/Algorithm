# BOJ_15654 N과 M (5)

from sys import setrecursionlimit

setrecursionlimit(10**5)

def dfs(level, number):
  if level == M:
    print(*answer)

  else:
      for i in range(1, N+1):
        if check[i] == 0:
          check[i] = 1
          answer[level] = data[i]
          dfs(level+1, i)
          check[i] = 0

N, M = map(int, input().split())
data = [0] + sorted(list(map(int, input().split())))

answer = [0] * M
check = [0] * (N+1)

dfs(0, 1)