# BOJ_1037 약수

from sys import stdin

input = stdin.readline

def solution():
    n = int(input().rstrip())
    divisor = sorted(list(map(int, input().rstrip().split())))

    print(divisor[0] * divisor[-1])

solution()