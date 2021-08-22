# BOJ_2869 달팽이는 올라가고 싶다

from sys import stdin

from math import ceil

input = stdin.readline

def solution():
    a, b, v = map(int, input().rstrip().split())

    print(ceil((v-a)/(a-b)) + 1)

solution()