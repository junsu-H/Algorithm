# BOJ_18310 안테나 S3

from sys import stdin

input = stdin.readline

N = int(input().rstrip())
home = sorted(list(map(int, input().rstrip().split())))

print(home[(N-1)//2])