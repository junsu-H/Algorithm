# BOJ_1758 알바생 강호

from sys import stdin

input = stdin.readline

def solution():
    n = int(input().rstrip())
    tips = sorted([int(input().rstrip()) for _ in range(n)], reverse=True)
    answer = 0

    for i in range(1, len(tips)+1):
        temp = tips[i-1] - (i-1)
        if temp > 0:
            answer += temp
    print(answer)
solution()