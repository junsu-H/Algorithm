# BOJ_1417 국회의원 선거

from sys import stdin

input = stdin.readline

def solution():
    n = int(input().rstrip())
    dasom = int(input().rstrip())
    candidate = [int(input().rstrip()) for i in range(n-1)]
    answer = 0

    while True:
        if len(candidate) == 0:
            break

        candidate.sort(reverse=True)
        if dasom > candidate[0]:
            break
        else:
            dasom += 1
            candidate[0] -= 1
            answer += 1

    print(answer)

solution()