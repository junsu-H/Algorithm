# BOJ_2576 홀수

import sys
sys.setrecursionlimit(10 ** 9)

def solution():
    array = []

    for i in range(7):
        tmp = int(sys.stdin.readline().rstrip())
        if tmp % 2 == 1:
            array.append(tmp)

    if len(array) == 0:
        print(-1)
    else:
        array.sort()
        print(sum(array))
        print(array[0])


solution()