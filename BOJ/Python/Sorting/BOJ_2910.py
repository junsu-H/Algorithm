# BOJ_2910 빈도 정렬

from sys import stdin
from collections import Counter

input = stdin.readline

def solution():
    n, m = map(int, input().rstrip().split())
    message = list(map(int, input().rstrip().split()))

    count = Counter(message)
    temp = []
    answer = ""

    for key, value in count.items():
        temp.append((key, value))
    
    temp.sort(key = lambda x: -x[1])

    for key, value in temp:
        answer += (str(key) + " ") * value

    print(answer)
    
solution()