# BOJ_1015 수열 정렬

import sys
sys.setrecursionlimit(10 ** 9)

def solution():
    n = int(sys.stdin.readline().rstrip())
    array = list(map(int, sys.stdin.readline().rstrip().split()))
        
    answer = [0] * n
    index = 0

    for i in range(n):
        min_index = array.index(min(array))
        array[min_index] = 9999
        answer[min_index] = index
        index += 1

    print(' '.join(map(str, answer)))

solution()