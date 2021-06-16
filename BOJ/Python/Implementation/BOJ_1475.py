# BOJ_1475 방 번호
import math
import sys
sys.setrecursionlimit(10 ** 9)

def solution():
    string = sys.stdin.readline().rstrip()
    answer = [0] * 10

    for i in string:
        i = int(i)
        if i == 6 or i == 9:
            answer[5] += 0.5
        else:
            answer[i] += 1

    print(math.ceil(max(answer)))

solution()