# BOJ_3059 등장하지 않는 문자의 합

import sys

sys.setrecursionlimit(10 ** 9)


def solution():
    n = int(sys.stdin.readline().rstrip())

    for _ in range(n):
        answer = 2015
        string = set(sys.stdin.readline().rstrip())

        for s in string:
            answer -= ord(s)
        print(answer)

solution()
