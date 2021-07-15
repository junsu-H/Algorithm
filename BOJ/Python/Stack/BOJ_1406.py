# BOJ_1406 에디터

from sys import stdin

input = stdin.readline

def solution():
    string = list(input().rstrip())
    m = int(input().rstrip())

    stack = []
    
    for _ in range(m):
        command = input().rstrip().split()
        if command[0] == "L" and len(string) > 0:
            stack.append(string.pop())
        elif command[0]== "D" and len(stack) > 0:
            string.append(stack.pop())
        elif command[0] == "B" and len(string) > 0:
            string.pop()
        elif command[0] == "P":
            string.append(command[1])

    print(''.join(string + stack[::-1]))

solution()