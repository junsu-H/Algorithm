import sys
import collections
sys.setrecursionlimit(10 ** 9)

def solution():
    n, k  = map(int, sys.stdin.readline().rstrip().split())

    answer = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]

    answer.sort(key = lambda x : (-x[1], -x[2], -x[3]))

    for i in range(n):
        if answer[i][0] == k:
            index = i
    
    for i in range(n):
        if answer[index][1:] == answer[i][1:]:
            print(i+1)
            break

solution()