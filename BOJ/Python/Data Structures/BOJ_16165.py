# BOJ_16165 걸그룹 마스터 준석이 S3

from collections import defaultdict
from sys import stdin

input = stdin.readline

N, M = map(int, input().rstrip().split())

girl_group = defaultdict(list)
solo = defaultdict()

for _ in range(N):
	group = input().rstrip()
	cnt = int(input().rstrip())

	for _ in range(cnt):
		member = input().rstrip()
		
		girl_group[group].append(member)
		solo[member] = group

for _ in range(M):
	question = input().rstrip()
	type = int(input().rstrip())

	if type == 0:
		girl_group[question].sort()
		for value in girl_group[question]:
			print(value)
		
	elif type == 1:
		print(solo[question])