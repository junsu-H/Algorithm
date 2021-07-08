# BOJ_14490 백대열

from sys import stdin
from math import gcd

input = stdin.readline

def solution():
    n, m = map(int, input().rstrip().split(":"))
    temp_gcd = gcd(n, m)

    print(str(n//temp_gcd) + ":" + str(m//temp_gcd))

solution()