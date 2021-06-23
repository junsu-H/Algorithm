# BOJ_2935 소음

import sys
sys.setrecursionlimit(10 ** 9)

def solution():
    a = int(sys.stdin.readline().rstrip())
    operator = sys.stdin.readline().rstrip()
    b = int(sys.stdin.readline().rstrip())
    
    if operator == "*":
        answer = a * b
    else:
        answer = a + b
    
    print(answer)
solution()