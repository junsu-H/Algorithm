# BOJ_18258 큐 2

from sys import stdin
from collections import deque

input = stdin.readline

def solution():
    n = int(input().rstrip())

    queue = deque()

    for i in range(n):
        operation = list(map(str, input().rstrip().split()))
        
        if operation[0] == "push":
            queue.append(operation[1])
        
        elif operation[0] == "pop":
            if queue:
                print(queue.popleft())
            else:
                print(-1)
        
        elif operation[0] == "size":
            print(len(queue))
        
        elif operation[0] == "empty":
            if len(queue):
                print(0)
            else:
                print(1)
        
        elif operation[0] == "front":
            if queue:
                print(queue[0])
            else:
                print(-1)

        elif operation[0] == "back":
            if queue:
                print(queue[-1])
            else:
                print(-1)

solution()