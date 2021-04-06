# BOJ_1152 단어의 개수

import sys
sys.setrecursionlimit(10 ** 9)

def solution():
    answer = list(map(str, sys.stdin.readline().rstrip().split()))

    print(len(answer))

solution()
