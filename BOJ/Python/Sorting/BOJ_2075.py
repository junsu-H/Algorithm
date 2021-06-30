# BOJ_2075 N번째 큰 수

import heapq
from sys import stdin

input = stdin.readline

def solution():
    n = int(input().rstrip())
    heap = []

    for _ in range(n):
        temp = list(map(int, input().rstrip().split()))

        if not heap:
            for t in temp:
                heapq.heappush(heap, t)
        else:
            for t in temp:
                if heap[0] < t:
                    heapq.heappush(heap, t)
                    heapq.heappop(heap)
    print(heap[0])

solution()