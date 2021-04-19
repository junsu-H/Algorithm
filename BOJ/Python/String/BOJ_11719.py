# BOJ_11719 그대로 출력하기 2

import sys
sys.setrecursionlimit(10 ** 9)

def solution():
    while True:
        try:
            print(input())
        except EOFError:
            break
        
solution()