# BOJ_2744 대소문자 바꾸기

import sys
sys.setrecursionlimit(10 ** 9)

def solution():
    string = sys.stdin.readline().rstrip()
    answer = []

    for i in range(len(string)):
        if string[i].isupper():
            answer.append(string[i].lower())
        else:
            answer.append(string[i].upper())

    print(''.join(map(str, answer)))

solution()