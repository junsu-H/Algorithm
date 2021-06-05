# BOJ_1120 문자열

import sys
sys.setrecursionlimit(10 ** 9)

def solution():
    a, b= map(str, sys.stdin.readline().rstrip().split())

    min_number = 999

    for i in range(len(b) - len(a) + 1):
        answer = 0
        
        for j in range(len(a)):
            if a[j] != b[i+j]:
                answer += 1

        min_number = min(min_number, answer)

    print(min_number)

solution()