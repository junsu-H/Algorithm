# BOJ_10799 쇠막대기

from sys import stdin

input = stdin.readline

def solution():
    bar = input().rstrip()
    stack, answer = [], 0

    for i in range(len(bar)):
        if bar[i] == "(":
            stack.append("(")
        else:
            if bar[i-1] == "(":
                stack.pop()
                answer += len(stack)
            else:
                stack.pop()
                answer += 1
    print(answer)

solution()