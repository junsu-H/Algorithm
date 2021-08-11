# BOJ_10800 컬러볼

from sys import stdin

from collections import defaultdict

input = stdin.readline

def solution():
    n = int(input().rstrip())
    ball = []
    answer = defaultdict(lambda: 0)
    size_sum = defaultdict(lambda: 0)
    j, total = 0, 0 

    for i in range(n):
        color, size = map(int, input().rstrip().split())
        ball.append([i, color, size])

    ball.sort(key=lambda x: x[2])

    for i in range(n):
        while True:
            if ball[i][2] <= ball[j][2]:
                break
    
            total += ball[j][2]
            size_sum[ball[j][1]] += ball[j][2]
            j += 1
        answer[ball[i][0]] = total - size_sum[ball[i][1]]  

    for i in range(n):
        print(answer[i])

solution()