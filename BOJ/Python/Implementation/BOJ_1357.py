# BOJ_1357 뒤집힌 덧셈

import sys
sys.setrecursionlimit(10 ** 9)

def solution():
    x, y = sys.stdin.readline().rstrip().split()

    print(int(str(int(x[::-1]) + int(y[::-1]))[::-1]))

solution()