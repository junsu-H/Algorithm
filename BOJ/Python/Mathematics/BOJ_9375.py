# BOJ_9375 패션왕 신해빈

from sys import stdin
from collections import Counter

input = stdin.readline

def solution():
    t = int(input().rstrip())

    for _ in range(t):
        answer = 1

        n = int(input().rstrip())

        clothes = [list(map(str, input().rstrip().split())) for _ in range(n)]
        count = Counter([value for key, value in clothes])
        
        for i in count.values():
            answer *= (i + 1)
        
        print(answer - 1)

solution()