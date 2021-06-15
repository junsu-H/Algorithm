# BOJ_15904 UCPC는 무엇의 약자일까?

import sys

sys.setrecursionlimit(10 ** 9)


def solution():
    string = sys.stdin.readline().rstrip()
    string_upper = []
    ucpc = ["U", "C", "P", "C"]

    answer = 0

    for s in string:
        if s.isupper():
            string_upper.append(s)

    for i in range(len(string_upper)):
        if string_upper[i] == ucpc[0] and answer == 0:
            answer += 1
        if string_upper[i] == ucpc[1] and answer == 1:
            answer += 1
        elif string_upper[i] == ucpc[2] and answer == 2:
            answer += 1
        elif string_upper[i] == ucpc[3] and answer == 3:
            answer += 1
            break

    if answer == 4:
        print("I love UCPC")
    else:
        print("I hate UCPC")

solution()