# BOJ_2874 게임을 만든 동준이

import sys
sys.setrecursionlimit(10 ** 9)

def solution():
    n = int(sys.stdin.readline().rstrip())
    array = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
    answer = 0
    
    for i in range(n-1, 0, -1):
        if array[i] <= array[i-1]:
            answer += (array[i-1] - array[i] + 1)
            array[i-1] = array[i] - 1
            
    print(answer)

solution()