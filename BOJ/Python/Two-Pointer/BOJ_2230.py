# BOJ_2230 수 고르기

import sys
sys.setrecursionlimit(10 ** 9)

def solution():
    n, m = map(int, sys.stdin.readline().rstrip().split())
    
    array = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
    array.sort()

    start, end = 0, 1
    answer = sys.maxsize

    while start < n and end < n :
        tmp =  array[end] - array[start]
        if tmp < m:
            end += 1
        else:
            start += 1
            answer = min(answer, tmp)
        
    print(answer)

solution()