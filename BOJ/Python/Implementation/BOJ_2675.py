# BOJ_2675 문자열 반복

import sys
sys.setrecursionlimit(10 ** 9)

def solution():
    n = int (sys.stdin.readline().rstrip())
    
    for i in range(n):
        answer = ''
        r, s = map(str, sys.stdin.readline().rstrip().split())
        
        for j in range(len(s)):
            answer += s[j] * int(r)
        
        print(answer)

solution()