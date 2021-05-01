# BOJ_2941 크로아티아 알파벳

import sys
sys.setrecursionlimit(10 ** 9)

def solution():
    alpha = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
    
    string = sys.stdin.readline().rstrip()

    for i in alpha:
        string = string.replace(i, '0')

    print(string)
    print(len(string))

solution()
