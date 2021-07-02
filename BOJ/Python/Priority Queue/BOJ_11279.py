# BOJ_11279 최대 힙

from sys import stdin
from heapq import heappush, heappop
input = stdin.readline

def solution():
    n = int(input().rstrip())
    heap = []

    for _ in range(n):
        x = int(input().rstrip())

        if x == 0:
            if len(heap) > 0:
                print(-heappop(heap))
            else:
                print(0)
        else:
            heappush(heap, -x)
    
solution()