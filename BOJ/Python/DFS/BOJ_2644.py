# BOJ_2644 촌수계산

from sys import setrecursionlimit

setrecursionlimit(10**5)

N = int(input())
x, y = map(int, input().split())
M = int(input())

graph = [ [] for _ in range(N+1)]
visit = [0] * (N+1)

for _ in range(M):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)

def dfs(value):
    for g in graph[value]:
        if visit[g] == 0:
            visit[g] = visit[value] + 1
            dfs(g)

dfs(x)
print(visit[y] if visit[y] > 0 else -1)