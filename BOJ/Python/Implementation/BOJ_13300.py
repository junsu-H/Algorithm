# BOJ_13300 방 배정 B2

from sys import stdin
from math import ceil

input = stdin.readline

N, K = map(int, input().rstrip().split())
students = [[0] * 7 for _ in range(2)] 

answer = 0

for _ in range(N):
	S, Y = map(int, input().rstrip().split())
	students[S][Y] += 1


for i in range(2):
	for j in range(1, 7):
		if students[i][j] == 0:
			continue

		answer += ceil(students[i][j] / K)

print(answer)