# BOJ_8958 OX퀴즈

import sys
sys.setrecursionlimit(10 ** 9)

def solution():
    n = int(sys.stdin.readline().rstrip())
    array = ''
    for _ in range(n):
        array = map(str, sys.stdin.readline().rstrip())
        answer = 0
        count = 0 
        for check in array:
            if check == 'O':
                count += 1
                answer += count
            else:
                count = 0
        print(answer)

solution()