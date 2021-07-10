# BOJ_13904 과제

from sys import stdin

input = stdin.readline

def solution():
    n = int(input().rstrip())
    homeworks = [list(map(int, input().rstrip().split())) for _ in range(n)]
    homeworks.sort(key=lambda x:-x[1])
    answer = [0] * 1001

    for h in homeworks:
        for j in range(h[0], 0, -1):
            if answer[j] == 0:
                answer[j] = h[1]
                break

    print(sum(answer))

solution()