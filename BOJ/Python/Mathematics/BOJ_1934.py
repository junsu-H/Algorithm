# BOJ_1934 최소공배수

from sys import stdin
from math import gcd

input = stdin.readline

def lcm(a, b):
    temp = gcd(a,b)
    return a * b // temp

def solution():
    t = int(input().rstrip())
    for _ in range(t):
        a, b = map(int, input().rstrip().split())
        print(lcm(a,b))

solution()