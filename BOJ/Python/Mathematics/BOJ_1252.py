# BOJ_1252 이진수 덧셈

from sys import stdin

input = stdin.readline

def solution():
    a, b = map(str, input().rstrip().split())
    a = int(a, 2)
    b = int(b, 2)
    answer = a + b

    print(bin(answer)[2:])    

solution()