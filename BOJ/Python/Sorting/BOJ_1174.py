# BOJ_1174 줄어드는 숫자

import sys
sys.setrecursionlimit(10 ** 9)
from itertools import combinations

def solution():
    n = int(sys.stdin.readline().rstrip())
    element = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    combi = []

    for ele in range(1, len(element) + 1):
        for c in list(combinations(element, ele)):
            temp = sorted(c, reverse=True)
            combi.append(''.join(map(str, temp)))
    
    combi = list(map(int, combi))
    combi.sort()

    try:
        print(combi[n-1])
    except:
        print(-1)
        
solution()
