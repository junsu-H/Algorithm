# BOJ_1652 누울 자리를 찾아라

import sys
sys.setrecursionlimit(10 ** 9)

def solution():
    n, m = map(int, sys.stdin.readline().rstrip().split())

    a = set(map(int, sys.stdin.readline().rstrip().split()))
    b = set(map(int, sys.stdin.readline().rstrip().split()))

    list_b = list(a-b)
    list_b.sort()
    
    print(len(a-b))
    print(' '.join(map(str, list_b)))

solution()