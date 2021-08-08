# BOJ_18310 안테나

from sys import stdin

input = stdin.readline

def solution():
    n = int(input().rstrip())
    home = list(map(int, input().rstrip().split()))
    home.sort()
    temp = 0

    for i in range(n//2):
        temp += (home[i] + home[-i])//2
    print(temp//2)

solution()