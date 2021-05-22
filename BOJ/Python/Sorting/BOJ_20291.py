# BOJ_20291 파일 정리

import sys
sys.setrecursionlimit(10 ** 9)
from collections import Counter

def solution():
    n = int(sys.stdin.readline().rstrip())
    array = [sys.stdin.readline().rstrip().split('.')[1] for _ in range(n)]
    
    keys_temp = list(Counter(array).keys())
    values_temp = list(Counter(array).values())
    answer = []

    for k, v in zip(keys_temp, values_temp):
        answer.append((k, v))

    answer.sort(key=lambda x: x[0])
    
    for k, v in answer:
        print(k, v)

solution()