# BOJ_5598 카이사르 암호

import sys
sys.setrecursionlimit(10 ** 9)

def solution():
    alpha = sys.stdin.readline().rstrip()

    for s in alpha:

        if 65 <= ord(s) and ord(s) <= 67:
            print(chr(ord(s) + 23), end ='')    
        else:
            print(chr(ord(s) - 3), end ='')

solution()