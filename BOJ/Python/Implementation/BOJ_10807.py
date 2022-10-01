# BOJ_10807 개수 세기

from sys import stdin

input = stdin.readline

N = int(input().rstrip())
data = list(map(int, input().rstrip().split()))
v = int(input().rstrip())

print(data.count(v))