# BOJ_11508 2+1 세일

import sys
sys.setrecursionlimit(10 ** 9)

def solution():
    n = int(sys.stdin.readline().rstrip())
    array = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
    array.sort(reverse=True)
    answer = 0

    for i in range(n):
        if (i % 3 != 2):
            answer += array[i]

    print(answer)            

solution()