# BOJ_1205 등수 구하기

import sys
sys.setrecursionlimit(10 ** 9)

def solution():
    n, new_score, p = map(int, sys.stdin.readline().rstrip().split())

    score = list(map(int, sys.stdin.readline().rstrip().split()))
    
    if len(score) == 0:
        score.append(new_score)
        score.sort(reverse=True)
        print(score.index(new_score)+1)
    elif score[-1] >= new_score and (len(score)+1) > p:
        print(-1)
    else:
        score.append(new_score)
        score.sort(reverse=True)
        print(score.index(new_score)+1)
    
solution()