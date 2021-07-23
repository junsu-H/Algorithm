# BOJ_2745 진법 변환

from sys import stdin

input = stdin.readline

def solution():
    n, b = input().rstrip().split()
    n = n[::-1]
    b = int(b)
    answer = 0
    
    for i in range(len(n)):
        temp = ord(n[i])
        if temp >= 48 and temp <= 57:
            temp -= 48
            answer += (b ** i) * temp
        else:
            temp -= 55
            answer += (b ** i) * temp
    print(answer)

solution()