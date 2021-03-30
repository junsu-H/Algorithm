# BOJ_11497 통나무 건너뛰기

import sys
sys.setrecursionlimit(10 ** 9)

def solution():
    t = int(sys.stdin.readline().rstrip())

    for _ in range(t):
        n = int(sys.stdin.readline().rstrip())
        array = list(map(int, sys.stdin.readline().rstrip().split()))
        array.sort()
        answer = 0
        
        for i in range(2, n):
            answer = max(answer, abs(array[i] - array[i-2]))        
        
        print(answer)

solution()