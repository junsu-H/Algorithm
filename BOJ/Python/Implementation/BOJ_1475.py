# BOJ_1475 방 번호

from math import ceil
from sys import stdin

input = stdin.readline

def solution():
    number = input().rstrip()
    answer = [0] * 10

    for n in number:
        n = int(n)
        if n == 6 or n == 9:
            answer[6] += 0.5
        else:
            answer[n] += 1

    print(ceil(max(answer)))

solution()