# BOJ_10988 팰린드롬인지 확인하기

import sys
sys.setrecursionlimit(10 ** 9)

def solution():
    string = sys.stdin.readline().rstrip()

    if string == string[::-1]:
        print(1)
    else:
        print(0)

solution()