# BOJ_10809 알파벳 찾기

import sys
sys.setrecursionlimit(10 ** 9)

def solution():
    alpha = sys.stdin.readline().rstrip()
    answer = dict()

    for i in range(97, 123):
        answer[chr(i)] = -1
    
    for i in range(len(alpha)):
        answer[alpha[i]] = alpha.index(alpha[i])

    for v in answer.values():
        print(v, end=' ')

solution()