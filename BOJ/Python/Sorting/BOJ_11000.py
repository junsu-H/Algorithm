import sys
import heapq 

def solution():
    n = int(sys.stdin.readline().rstrip())

    array = []
    heap = []

    for _ in range(n):
        array.append(list(map(int, sys.stdin.readline().rstrip().split())))

    array.sort(key=lambda x: x[0])

    for i in range(n):
        if len(heap) != 0 and heap[0] <= array[i][0]:
            heapq.heappop(heap)
        heapq.heappush(heap, array[i][1])

    print(len(heap))

solution()