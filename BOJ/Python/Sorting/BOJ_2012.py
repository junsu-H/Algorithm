# BOJ_2012 등수 매기기

import sys
sys.setrecursionlimit(10 ** 9)

def solution():
    n = int(sys.stdin.readline().rstrip())
    array = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
    array.sort()
    answer = 0

    for i in range(n):
        answer += abs(array[i]-(i+1))

    print(answer)
    
solution()