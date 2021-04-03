# BOJ_2606 바이러스

import sys
from collections import deque
sys.setrecursionlimit(10 ** 9)

def solution():
    n = int(sys.stdin.readline().rstrip())
    m = int(sys.stdin.readline().rstrip())
    
    graph = [[0] * (n + 1) for _ in range(n + 1)]  
    visited = [False] * (n+1)
    answer = []

    for _ in range(m):
        x, y = map(int, sys.stdin.readline().rstrip().split())
        graph[x][y] = 1
        graph[y][x] = 1
    
    print(dfs(graph, 1, visited, answer))
    
def dfs(graph, v, visited, answer):
    visited[v] = True

    for i in range(1, len(graph)):
        if not visited[i] and graph[v][i] == 1:
            answer.append(v)
            dfs(graph, i, visited, answer)
    return len(answer)

solution()