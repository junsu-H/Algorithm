# BOJ_1978 소수 찾기

from sys import stdin
from math import gcd

input = stdin.readline

def solution():
    n = int(input().rstrip())
    prime_num = list(map(int, input().rstrip().split()))
    answer = 0

    for p in prime_num:
        for i in range(2, p):
            if p % i == 0:
                break
        else:
            if p != 1:
                answer += 1
    print(answer)

solution()