# BOJ_2164 카드2

from sys import stdin

from collections import deque

input = stdin.readline

def solution():
    n = int(input().rstrip())
    queue = deque(range(1, n+1))

    while True:
        if len(queue) == 1:
            print(queue.popleft())
            break
        
        queue.popleft()
        queue.append(queue.popleft())

solution()