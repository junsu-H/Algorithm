# BOJ_3986 좋은 단어

from sys import stdin

input = stdin.readline

def solution():
    n = int(input().rstrip())
    answer = 0

    for _ in range(n):
        temp = input().rstrip()
        stack = []

        for t in temp:
            if not stack or stack[-1] != t:
                stack.append(t)
            else:
                stack.pop()
        
        if not stack:
            answer += 1
        
    print(answer)

solution()