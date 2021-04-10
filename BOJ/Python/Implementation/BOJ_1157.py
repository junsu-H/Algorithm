# BOJ_1157 단어 공부

import sys
sys.setrecursionlimit(10 ** 9)
from collections import Counter

def solution():
    string = sys.stdin.readline().rstrip().lower()
    answer = Counter(string).most_common(2)

    if len(string) == 1:
        print(answer[0][0].upper())
    else:
        if answer[0][1] == answer[1][1]:
            print('?')
        else:
            print(answer[0][0].upper())

solution()