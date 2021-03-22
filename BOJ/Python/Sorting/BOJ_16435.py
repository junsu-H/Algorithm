# 스네이크버드

import sys
sys.setrecursionlimit(10 ** 9)

def solution():
    n, l= map(int, sys.stdin.readline().rstrip().split())
    array = list(map(int, sys.stdin.readline().rstrip().split()))
    array.sort()

    for i in range(n):
        if l >= array[i]:
            l += 1
    
    print(l)

solution()
