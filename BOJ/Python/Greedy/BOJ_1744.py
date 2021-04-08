# BOJ_1744 수 묶기

import sys
sys.setrecursionlimit(10 ** 9)

def solution():
    n = int(sys.stdin.readline().rstrip())
    
    positive = []
    negative = []
    answer = 0

    for _ in range(n):
        i = int(sys.stdin.readline().rstrip())
        if i > 0 :
            positive.append(i)
        elif i <= 0:
            negative.append(i)
    
    positive.sort()
    negative.sort(reverse=True)

    while True:
        if len(positive) == 0 and len(negative) == 0:
            break
        if len(positive) >= 2:
            a = positive.pop()
            b = positive.pop()
            answer += max(a * b, a + b)
        elif len(negative) >= 2:
            a = negative.pop()
            b = negative.pop()
            answer += max(a * b, a + b)
        elif len(positive) == 1:
            a = positive.pop()
            answer += a
        elif len(negative) == 1:
            b = negative.pop()
            answer += b
        
    print(answer)

solution()