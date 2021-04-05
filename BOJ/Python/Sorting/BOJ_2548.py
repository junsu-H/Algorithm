# BOJ_2548 대표 자연수

import sys
sys.setrecursionlimit(10 ** 9)

def solution():
    n = int(sys.stdin.readline().rstrip())
    array = list(map(int, sys.stdin.readline().rstrip().split()))
    
    array.sort()

    if len(array) % 2 == 0:
        print(array[len(array)//2 -1])
    else:
        print(array[len(array)//2])

solution()

