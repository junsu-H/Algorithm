# BOJ_18870 좌표 압축

import sys
sys.setrecursionlimit(10 ** 9)

def solution():
    n = int(sys.stdin.readline().rstrip())
    array = list(map(int, sys.stdin.readline().rstrip().split()))
    sorted_arrry = sorted(list(set(array)))
    dic = {sorted_arrry[i]: i for i in range(len(sorted_arrry))}

    for i in array:
        print(dic[i], end = ' ')

solution()