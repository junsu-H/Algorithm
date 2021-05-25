# BOJ_11365 !밀비 급일

import sys
sys.setrecursionlimit(10 ** 9)

def solution():
    while True:
        string = sys.stdin.readline().rstrip()
        if string == 'END':
            break
        else:
            print(string[::-1])
    
solution()