# BOJ_10798 세로읽기

import sys
sys.setrecursionlimit(10 ** 9)

def solution():
    string = [sys.stdin.readline().rstrip() for _ in range(5)]

    for i in range(max(map(lambda x:len(x), string))):
        for j in range(5):
            if i < len(string[j]):
                print(string[j][i], end='')
    
solution()