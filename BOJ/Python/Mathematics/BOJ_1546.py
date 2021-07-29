# BOJ_1546 평균

from sys import stdin

input = stdin.readline

def solution():
    n = int(input().rstrip())
    score = list(map(int, input().rstrip().split()))

    max_score = max(score)

    for i in range(len(score)):
        score[i] = score[i]/max_score*100
    
    print(sum(score)/n)

solution()