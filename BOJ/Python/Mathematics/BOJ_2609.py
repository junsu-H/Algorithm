# BOJ_2609 최대공약수와 최소공배수

from sys import stdin
from math import gcd

input = stdin.readline

def lcm(a, b):
    temp = gcd(a,b)
    return a * b // temp

def solution():
    a, b = map(int, input().rstrip().split())
    print(gcd(a,b))
    print(lcm(a,b))

solution()