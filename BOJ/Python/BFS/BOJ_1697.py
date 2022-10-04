# BOJ_1697 숨바꼭질 S1

from sys import stdin
from collections import deque

input = stdin.readline

N, K = map(int, input().rstrip().split())

max_num = 100_001
visited = [0] * max_num

q = deque([(N, 0)])
while q:
	# 위치, 시간
	location, sec = q.popleft()

	if location == K:
		print(sec)
		break
	
	# 경우의 수 3가지
	for l in (location-1, location+1, location*2):
		# 최대로 갈 수 있는 위치, 한 번 방문했는지 확인
		if 0 <= l < max_num and visited[l] == 0:
			visited[l] = 1
			q.append((l, sec+1))