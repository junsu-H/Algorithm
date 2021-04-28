# BOJ_1783 병든 나이트

import sys
sys.setrecursionlimit(10 ** 9)

def solution():
    n, m = map(int, sys.stdin.readline().rstrip().split())

    answer = 0
    if n == 1:
        answer = 1
    elif n == 2:
        answer = min(4, (m + 1)//2)
    else:
        if m < 7:
            answer = min(4, m)
        else:
            answer = m - 2
    
    print(answer)

solution()