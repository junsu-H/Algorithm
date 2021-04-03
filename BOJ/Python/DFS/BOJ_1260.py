# BOJ_1260 DFS와 BFS

import sys
from collections import deque
sys.setrecursionlimit(10 ** 9)

def solution():
    n, m, v = map(int, sys.stdin.readline().rstrip().split())
    graph = [[0] * (n + 1) for _ in range(n + 1)]  
    visited = [False] * (n+1)

    for _ in range(m):
        x, y = map(int, sys.stdin.readline().rstrip().split())
        graph[x][y] = 1
        graph[y][x] = 1
    
    print(graph)
    dfs(graph, v, visited)
    
    visited = [False] * (n+1)

    print()
    bfs(graph, v, visited)

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')

    for i in range(1, len(graph)):
        if not visited[i] and graph[v][i] == 1:
            dfs(graph, i, visited)

def bfs(graph, v, visited):
    queue = deque([v])
    visited[v] = True

    while queue:
        v = queue.popleft()
        print(v, end = ' ')
        for i in range(1, len(graph)):
            if not visited[i] and graph[v][i] == 1:
                queue.append(i)
                visited[i] = True

solution()