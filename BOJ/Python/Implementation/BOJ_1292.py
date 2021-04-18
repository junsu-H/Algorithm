# BOJ_1292 쉽게 푸는 문제

import sys
sys.setrecursionlimit(10 ** 9)

def solution():
    a, b = map(int, sys.stdin.readline().rstrip().split())  

    seq = []

    for i in range(1, 46):
        seq += [i] * i

    print(sum(seq[a-1:b]))

solution()