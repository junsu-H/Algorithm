# BOJ_17608 막대기

import sys
sys.setrecursionlimit(10**9)

def solution():
    n = int(sys.stdin.readline().rstrip())
    bar = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
    max_bar= 0
    answer = 0

    while len(bar) != 0:
        tmp = bar.pop()
        
        if max_bar < tmp:
            max_bar = tmp
            answer += 1
            

    print(answer)

solution()
