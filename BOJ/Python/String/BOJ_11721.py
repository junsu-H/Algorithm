# BOJ_11721 열 개씩 끊어 출력하기

import sys
sys.setrecursionlimit(10 ** 9)

def solution():
    n = sys.stdin.readline().rstrip()
    
    for i in range(0, len(n), 10):
        print(n[i:i+10])
solution()