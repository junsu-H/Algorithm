# BOJ_17299 오등큰수

from sys import stdin
from collections import Counter

input = stdin.readline

def solution():
    n = int(input().rstrip())
    seq = list(map(int, input().rstrip().split()))
    count = Counter(seq)
    seq = [(s, count[s]) for s in seq]
    print(seq)

    stack = [0]
    answer = [-1] * n

    for i in range(1, n):
        while stack and seq[stack[-1]][1] < seq[i][1]:
            answer[stack.pop()] = seq[i][0]
        stack.append(i)

    print(*answer)
    
solution()