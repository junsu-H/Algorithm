# BOJ_2170 선 긋기

import sys
sys.setrecursionlimit(10 ** 9)

def solution():
    n = int(sys.stdin.readline().rstrip())
    
    array = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
    array.sort(key = lambda x: (x[0], -x[1]))

    start = array[0][0]
    end = array[0][1]
    answer = 0

    for i in range(1, n):
        if end > array[i][0]:
            if end > array[i][1]:
                continue
            else:
                end = array[i][1]
        else:
            answer += (end - start)
            start = array[i][0]
            end = array[i][1]
    
    answer += (end - start)
    print(answer)

solution()