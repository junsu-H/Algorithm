# BOJ_14729 칠무해

import sys
sys.setrecursionlimit(10 ** 9)

def solution():
    n = int(sys.stdin.readline().rstrip())
    array = [float(sys.stdin.readline().rstrip()) for _ in range(n)]
    array.sort()

    for i in range(7):
        print(format(array[i],".3f"))

solution()