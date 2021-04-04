# BOS_11724 연결 요소의 개수

import sys
sys.setrecursionlimit(10000)

def dfs(graph, v, visited):
    visited[v] = True
    
    for i in range(1, len(graph)):
        if not visited[i] and graph[v][i] == 1:
            dfs(graph, i, visited)

def solution():
    n, m = map(int, sys.stdin.readline().rstrip().split())    
    graph = [[0] * (n + 1) for _ in range(n + 1)]
    visited = [False] * (n + 1)
    answer = 0

    for _ in range(m):
        u, v = map(int, sys.stdin.readline().rstrip().split())
        graph[u][v] = 1
        graph[v][u] = 1


    for i in range(1, n + 1): 
        if not visited[i]: 
            dfs(graph, i, visited) 
            answer += 1
    
    print(answer)

solution()