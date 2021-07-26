# BOJ_15650 N과 M (2)

from sys import stdin
from itertools import combinations

input = stdin.readline

def solution():
    n, m = map(int, input().rstrip().split())
    combi = combinations(range(1, n+1), m)

    for c in combi:
        print(*c)
        # print(' '.join(map(str, c))) 

solution()