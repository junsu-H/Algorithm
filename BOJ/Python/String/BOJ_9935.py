# BOJ_9935 문자열 폭발

from sys import stdin

input = stdin.readline

def solution():
    string = input().rstrip()
    bomb = input().rstrip()
    stack = []

    for s in string:
        stack.append(s)
        if "".join(stack[-len(bomb):]) == bomb:
            del stack[-len(bomb):]

    if len(stack) == 0:
        print("FRULA")
    else:
        print("".join(map(str, stack)))
    
solution()