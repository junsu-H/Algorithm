# BOJ_1202 보석 도둑

import sys
sys.setrecursionlimit(10 ** 9)
import heapq

def solution():
    n, k = map(int, sys.stdin.readline().rstrip().split())

    jewelry  = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
    bag_weight = [int(sys.stdin.readline().rstrip()) for _ in range(k)]
    jewelry.sort()
    bag_weight.sort()

    temp = []
    answer = 0
    for i in range(len(bag_weight)):
        while jewelry and bag_weight[i] >= jewelry[0][0]:
            heapq.heappush(temp, -jewelry[0][1])
            heapq.heappop(jewelry)
        
        if temp:
            answer -= heapq.heappop(temp)
        elif not jewelry:
            break
    print(answer)

solution()