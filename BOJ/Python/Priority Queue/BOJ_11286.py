# BOJ_11286 절댓값 힙

from sys import stdin
from heapq import heappop, heappush

input = stdin.readline

def solution():
    n = int(input().rstrip())
    heap = []
    for i in range(n): 
        x = int(input().rstrip())
        if x == 0:
            if len(heap) > 0:
                print(heappop(heap)[1])
            else:
                print(0)
        else:
            heappush(heap, (abs(x), x))

solution()