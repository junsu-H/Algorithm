# BOJ_1427 소트인사이드

import sys
sys.setrecursionlimit(10 ** 9)

def solution():
    n = sys.stdin.readline().rstrip()
    
    result = [] 

    for i in range(len(n)):
        result.append(int(n[i]))

    result.sort(reverse=True)

    print(''.join(map(str, result)))

solution()
