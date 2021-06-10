# BOJ_9237 이장님 초대

import sys
sys.setrecursionlimit(10000)

def dfs(graph, v, visited):
        pass

def solution():
    n = int(sys.stdin.readline().rstrip())
    tree = list(map(int, sys.stdin.readline().rstrip().split()))
    tree.sort(reverse=True)
    answer =  0

    for i, j in enumerate(tree):
        answer = max(answer, i + j + 2)

    print(answer)
solution()