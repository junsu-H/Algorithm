# BOJ_2812 크게 만들기

import sys
sys.setrecursionlimit(10**9)

def solution():
    n, k = map(int, sys.stdin.readline().rstrip().split())
    diff = int(n-k)
    number = list(map(str, sys.stdin.readline().rstrip()))
    answer = []
    
    for i in range(n):
        while answer and k > 0:
            if answer[-1] < number[i]:
                answer.pop()
                k -= 1
            else:
                break
        answer.append(number[i])

    print(''.join(answer[:diff]))

solution()