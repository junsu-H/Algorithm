# # BOJ_1655 가운데를 말해요

from heapq import heappush, heappop
from sys import stdin

input = stdin.readline

def solution():
    n = int(input().rstrip())
    max_heap, min_heap = [], []

    for _ in range(n):
        x = int(input().rstrip())
        if len(min_heap) == len(max_heap):
            heappush(max_heap,-x)
        else:
            heappush(min_heap,x)
        
        if min_heap and -max_heap[0] > min_heap[0]:
            heappush(max_heap, -heappop(min_heap))
            heappush(min_heap, -heappop(max_heap))

        print(-max_heap[0])

solution()