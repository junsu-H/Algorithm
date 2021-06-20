# BOJ_17413 단어 뒤집기

import sys

sys.setrecursionlimit(10 ** 9)


def solution():
    string = sys.stdin.readline().rstrip()
    answer = ""
    reverse = True
    word = ""

    for s in string:
        if s == "<":
            reverse = False
            answer += word
            word = s
        elif s == ">":
            reverse = True
            answer += word + s
            word = ""
        elif s == " ":
            answer += (word + s)
            word = ""
        elif reverse:
            word = s + word
        else:
            word += s

    print(answer + word)


solution()
