# BOJ_9093 단어 뒤집기

import sys
sys.setrecursionlimit(10 ** 9)

def solution():
    n = int(sys.stdin.readline().rstrip())
    array = [list(map(str, sys.stdin.readline().rstrip().split())) for _ in range(n)]

    for i in range(n):
        for j in range(len(array[i])):
            print(array[i][j][::-1], end = ' ')
        print()

solution()