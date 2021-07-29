# BOJ_4344 평균은 넘겠지

from sys import stdin

input = stdin.readline

def solution():
    c = int(input().rstrip())
    
    for i in range(c):
        case = list(map(int, input().rstrip().split()))
        avg = sum(case[1:]) / case[0]
        answer = 0

        for j in case[1:]:
            if j > avg:
                answer += 1
        print("{:.3f}%".format(answer / case[0] * 100))

solution()