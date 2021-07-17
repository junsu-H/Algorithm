# BOJ_1476 날짜 계산

from sys import stdin

input = stdin.readline

def solution():
    e, s, m = map(int, input().rstrip().split())
    answer = 0
    i, j, k = 0, 0, 0
    while True:
        i = (i % 15) + 1
        j = (j % 28) + 1
        k = (k % 19) + 1
        answer += 1
        if i == e and j == s and k == m:
            print(answer)
            break
solution()