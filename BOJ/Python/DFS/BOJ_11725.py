# BOJ_11725 트리의 부모찾기

import sys
sys.setrecursionlimit(10 ** 9)

n = int(sys.stdin.readline().rstrip())

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
parent = {}

def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            parent[i] = v
            dfs(i)

def solution():
    for _ in range(n - 1):
        x, y = map(int, sys.stdin.readline().rstrip().split())
        graph[x].append(y)
        graph[y].append(x)

    dfs(1)

    for i in range(2, n+1):
        print(parent[i])

solution()