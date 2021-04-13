# BOJ_1806 부분합

import sys
sys.setrecursionlimit(10 ** 9)

def solution():
    n, m = map(int, sys.stdin.readline().rstrip().split())

    array = list(map(int, sys.stdin.readline().rstrip().split()))

    start, end = 0, 1
    interval_sum = array[0]
    answer = sys.maxsize

    while start <= end:
        if interval_sum >= m:
            answer = min(answer, end-start)
            interval_sum -= array[start]
            start += 1
        elif end == n:
            break
        else:
            interval_sum += array[end]
            end += 1
            
    if answer == sys.maxsize:
        print(0)
    else:
        print(answer)

solution()