# BOJ_1100 하얀 칸

import sys
sys.setrecursionlimit(10 ** 9)

def solution():
    chess = [list(map(str, sys.stdin.readline().rstrip())) for _ in range(8)]
    answer = 0

    for i in range(8):
        for j in range(8):
            if (i+j) % 2 == 0 and chess[i][j] == 'F':
                answer += 1
    
    print(answer)
    
solution()