# BOJ_14241 슬라임 합치기

from sys import stdin

input = stdin.readline

def solution():
    n = int(input().rstrip())
    scores = list(map(int, input().rstrip().split()))
    answer =  0

    for i in range(1, n):
        answer += scores[i-1] * scores[i]
        scores[i] += scores[i-1]
    
    print(answer)

solution()