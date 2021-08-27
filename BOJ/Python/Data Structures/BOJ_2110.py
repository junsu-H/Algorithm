# BOJ_10866 덱

from sys import stdin
from collections import deque

input = stdin.readline

def solution():
    n = int(input().rstrip())
    d = deque()

    for _ in range(n):
        operation = list(input().rstrip().split())

        if operation[0] == "push_front":
            d.appendleft(operation[1])
        
        elif operation[0] == "push_back":
            d.append(operation[1])
        
        elif operation[0] == "pop_front":
            if len(d):
                print(d.popleft())
            else:
                print(-1)
        
        elif operation[0] == "pop_back":
            if len(d):
                print(d.pop())
            else:
                print(-1)
        
        elif operation[0] == "size":
            print(len(d))

        elif operation[0] == "empty":
            if len(d):
                print(0)
            else:
                print(1)

        elif operation[0] == "front":
            if len(d):
                print(d[0])
            else:
                print(-1)
        
        elif operation[0] == "back":
            if len(d):
                print(d[-1])
            else:
                print(-1)

solution()