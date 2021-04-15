# BOJ_1159 농구 경기

import sys
sys.setrecursionlimit(10 ** 9)

def solution():
    n = int(sys.stdin.readline().rstrip())
    if n < 5:
        print("PREDAJA")
        return

    check = [0] * 26
    alpa = 'abcdefghijklmnopqrstuvwxyz'

    answer = []

    for _ in range(n):
        name = sys.stdin.readline().rstrip()
        check[alpa.index(name[0])] += 1

    for i in range(len(alpa)):
        if check[i] >= 5:
            answer.append(alpa[i])

    if not answer:
        print("PREDAJA")
    else:
        print(''.join(map(str, answer)))

solution()