# BOJ_13305 주유소

import sys
sys.setrecursionlimit(10 ** 9)

def solution():
    n = int(sys.stdin.readline().rstrip())

    liter = list(map(int, sys.stdin.readline().rstrip().split()))
    city = list(map(int, sys.stdin.readline().rstrip().split()))

    answer = liter[0] * city[0]
    temp = city[0]

    for i in range(1, n-1):
        if city[i] < temp:
            temp = city[i]
        answer += temp * liter[i]

    print(answer)    
    
solution()