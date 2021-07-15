# BOJ_10845 큐

from sys import stdin

input = stdin.readline

def solution():
    queue = []

    n = int(input().rstrip())

    for i in range(n):
        command = input().rstrip().split()

        if command[0] == "push":
            queue.append(command[1])
        
        elif command[0] == "pop":
            if queue:
                print(queue.pop(0))
            else:
                print(-1)
        elif command[0] == 'size': 
            print(len(queue))
        elif command[0] == "front":
            if len(queue) == 0:
                print(-1)
            else:
                print(queue[0])
        elif command[0] == "back":
            if len(queue) == 0:
                print(-1)
            else:
                print(queue[-1])
        elif command[0] == "empty":
            if len(queue) == 0:
                print(1)
            else:
                print(0)

solution()