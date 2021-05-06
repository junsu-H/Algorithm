# BOJ_1032 명령 프롬프트

import sys
sys.setrecursionlimit(10 ** 9)

def solution():
    n = int(sys.stdin.readline().rstrip())

    
    answer = ''

    array  = [str(sys.stdin.readline().rstrip()) for _ in range(n)]

    temp = list(array[0])

    
    for i in range(1, len(array)):
        for j in range(len(array[0])):
            if temp[j] == array[i][j]:
                continue
            else:
                temp[j] = '?'

    print(''.join(temp))

solution()