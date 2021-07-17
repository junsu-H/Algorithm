# BOJ_1254 팰린드롬 만들기

import sys
sys.setrecursionlimit(10 ** 9)

def solution():
    s = sys.stdin.readline().rstrip()
    
    for i in range(len(s)):
        if s[i:] == s[i:][::-1]:
            print(i + len(s))
            break
    
solution()