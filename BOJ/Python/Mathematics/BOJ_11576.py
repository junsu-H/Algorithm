# BOJ_11576 Base Conversion

from sys import stdin

input = stdin.readline

def solution():
    a, b = map(int, input().rstrip().split())
    m = int(input().rstrip())
    digits = list(map(int, input().rstrip().split()))[::-1]
    ten = 0
    answer = []

    for i in range(len(digits)):
        ten += digits[i] * (a ** i)
    
    while True:
        if ten == 0:
            break
        answer.append(ten % b)
        ten //= b

    print(*answer[::-1])

solution()