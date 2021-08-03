# BOJ_10824 네 수

from sys import stdin

input = stdin.readline

def solution():
    a, b, c, d = map(str, input().rstrip().split())

    print(int(a+b) + int(c+d))

solution()