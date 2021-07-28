# BOJ_1676 팩토리얼 0의 개수

from sys import stdin

input = stdin.readline

def solution():
    n = int(input().rstrip())
    answer = 0
    while True:
        if n < 5:
            break
        
        answer += (n // 5)
        n //= 5
    
    print(answer)
        
solution()