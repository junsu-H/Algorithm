# BOJ_13333 Q-인덱스

from sys import stdin

input = stdin.readline

def solution():
    n = int(input().rstrip())
    array = list(map(int, input().rstrip().split()))
    array.sort(reverse = True)

    answer = 0
    for i in range(len(array)):
        if array[i] > answer:
            answer += 1
        else:
            break
    print(answer)

solution()