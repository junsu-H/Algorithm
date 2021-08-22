# BOJ_3052 나머지

from sys import stdin

input = stdin.readline

def solution():
    answer = set()
    for _ in range(10):
        n = int(input().rstrip())
        answer.add(n % 42)
        
    print(len(answer))

solution()