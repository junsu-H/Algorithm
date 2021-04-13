# BOJ_11720 숫자의 합

import sys
sys.setrecursionlimit(10 ** 9)

def solution():
    n = int(sys.stdin.readline().rstrip())
    number = list(map(int, sys.stdin.readline().rstrip()))

    print(sum(number))
    
solution()
