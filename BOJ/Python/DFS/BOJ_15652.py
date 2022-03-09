# BOJ_15652 N과 M (4)

from sys import setrecursionlimit

setrecursionlimit(10**5)

def dfs(level, number):
  if level == M:
    print(*answer)

  else:
      for i in range(number, N+1):
            check[i] = 1
            answer[level] = i
            dfs(level+1, i)
            check[i] = 0

N, M = map(int, input().split())
answer = [0] * M
check = [0] * (N+1)

dfs(0, 1)