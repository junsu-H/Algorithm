# BOJ_1759 암호 만들기

import sys
sys.setrecursionlimit(10 ** 9)
from itertools import combinations

def solution():
    l, c = map(int, sys.stdin.readline().rstrip().split())
    array = sorted(list(map(str, sys.stdin.readline().rstrip().split())))
    vowel = set('aeiou')

    combi = list(combinations(array, l))
    
    for c in combi:
        temp = set(c) - vowel
        if len(temp) >= 2:
            if l-len(temp) >= 1:
                print(''.join(c))
    
solution()