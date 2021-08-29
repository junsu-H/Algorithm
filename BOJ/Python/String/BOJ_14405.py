# BOJ_14405 피카츄

from sys import stdin

from re import sub

input = stdin.readline

def solution():
    string = input().rstrip()

    string = sub("pi|ka|chu", '', string)

    if not string:
        print("YES")
    else:
        print("NO")
        
solution()