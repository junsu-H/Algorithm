# BOJ_2902 KMP는 왜 KMP일까?

import sys
sys.setrecursionlimit(10 ** 9)

def solution():
    string = list(map(str, sys.stdin.readline().rstrip().split('-')))

    for s in string:
        print(s[0], end ='')

solution()