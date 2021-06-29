# BOJ_9251 LCS

import sys
sys.setrecursionlimit(10 ** 9)

def solution():
    first = sys.stdin.readline().rstrip()
    second =  sys.stdin.readline().rstrip()
    
    array = [[0] * (len(first) + 1) for _ in range(len(second) + 1)]
    for i in range(1, len(second) + 1):
        for j in range(1, len(first) + 1):
            if first[j-1] == second[i-1]:
                array[i][j] = array[i-1][j-1] + 1
            else:
                array[i][j] = max(array[i-1][j], array[i][j-1])

    print(array[len(second)][len(first)])

solution()

