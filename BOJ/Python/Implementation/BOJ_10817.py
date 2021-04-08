# BOJ_10817 세 수

import sys
sys.setrecursionlimit(10 ** 9)

def solution():
    array = list(map(int, sys.stdin.readline().rstrip().split()))

    array.sort()

    print(array[1])
    
solution()