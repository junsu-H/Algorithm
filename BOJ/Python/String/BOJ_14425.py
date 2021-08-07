# BOJ_14425 문자열 집합

from sys import stdin

input = stdin.readline

def solution():
    n, m = map(int, input().rstrip().split())
    set_n = {input().rstrip() for _ in range(n)}
    answer = 0

    for _ in range(m):
        string = input().rstrip()
        if string in set_n:
            answer += 1

    print(answer)
    
solution()