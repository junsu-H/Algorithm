# BOJ_2109 순회강연

from sys import stdin

from heapq import heappop, heappush

input = stdin.readline

def solution():
    n = int(input().rstrip())
    lecture = sorted([list(map(int, input().rstrip().split())) for _i in range(n)], key=lambda x: (x[1], -x[0]))

    answer = []
    for i in range(n):
        heappush(answer, lecture[i][0])
        if len(answer) > lecture[i][1]:
            heappop(answer)
    
    print(sum(answer))

solution()