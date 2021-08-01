# BOJ_2501 약수 구하기

from sys import stdin

input = stdin.readline

def solution():
    p, q = map(int, input().rstrip().split())
    answer = [i for i in range(1, p+1) if p % i == 0]

    try:
        print(answer[q-1])
    except:
        print(0)

solution()