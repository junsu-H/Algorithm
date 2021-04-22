# BOJ_10953 A+B - 6

import sys
sys.setrecursionlimit(10 ** 9)

def solution():
    t = int(sys.stdin.readline().rstrip())
    
    for _ in range(t):
        array = list(map(int, sys.stdin.readline().rstrip().split(',')))
        print(sum(array))

solution()