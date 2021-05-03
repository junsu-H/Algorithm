# BOJ_2908 상수

import sys
sys.setrecursionlimit(10 ** 9)

def solution():
    n, m = map(str, sys.stdin.readline().rstrip().split())
    
    if n[::-1] > m[::-1]:
        print(n[::-1])
    else:
        print(m[::-1])

solution()