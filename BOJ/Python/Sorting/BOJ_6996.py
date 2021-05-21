# BOJ_6996 애너그램

import sys
sys.setrecursionlimit(10 ** 9)

def solution():
    n = int(sys.stdin.readline().rstrip())

    for _ in range(n):
        a, b = map(str, sys.stdin.readline().rstrip().split())
        
        if (sorted(list(a)) == sorted(list(b))):
            print(a, "&", b, "are anagrams.")
        else:
            print(a, "&", b, "are NOT anagrams.")
    
solution()