# BOJ_1789 수들의 합

import sys
import heapq

def solution():
    n = int(sys.stdin.readline().rstrip())
    
    hap = 0
    i = 0

    while True:
        if hap + i >= n:
            break
        else:
            i += 1
            hap += i
    
    print(i)

solution()