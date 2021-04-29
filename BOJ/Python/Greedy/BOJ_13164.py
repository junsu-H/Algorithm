# BOJ_13164 행복 유치원

import sys
sys.setrecursionlimit(10 ** 9)

def solution():
    n, m = map(int, sys.stdin.readline().rstrip().split())
    array = list(map(int, sys.stdin.readline().rstrip().split()))
    dp = []
    
    for i in range(n-1):
        dp.append(array[i + 1] - array[i])
    
    dp.sort()

    print(sum(dp[:n-m]))

solution()