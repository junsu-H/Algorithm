# BOJ_17298 오큰수

from sys import stdin

input = stdin.readline

def solution():
    n = int(input().rstrip())
    seq = list(map(int, input().rstrip().split()))

    stack = [0]
    answer = [-1] * n

    for i in range(1, n):
        while stack and seq[stack[-1]] < seq[i]:
            answer[stack.pop()] = seq[i]
        stack.append(i)

    print(*answer)
    
solution()