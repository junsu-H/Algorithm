import sys

def solution():
    input = sys.stdin.readline
    INF = int(1e9)

    n, m = map(int, input().split())

    start = int(input())

    graph = [[] for _ in range(n+1)]
    
    visited = [False] * (n+1)

    distance = [INF] * (n+1)

    # 모든 간선 정보를 입력받기
    for _ in range(m):
        from_node, to_node, cost = map(int, input().split())


solution()

    