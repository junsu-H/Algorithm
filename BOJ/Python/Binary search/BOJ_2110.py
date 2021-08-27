# BOJ_2110 공유기 설치

from sys import stdin

input = stdin.readline

def solution():
    n, c = map(int, input().rstrip().split())

    house = sorted([int(input().rstrip()) for _ in range(n)])

    start, end = 1, house[-1] - house[0]
    answer = 0

    while True:
        if start > end:
            break

        mid = (start + end) // 2
        count = 1
        pre_house = house[0]

        for i in range(1, n):
            if house[i] - pre_house >= mid:
                count += 1
                pre_house = house[i]

        if count >= c:
            start = mid + 1
            answer = mid
        else:
            end = mid - 1

    print(answer)

solution()