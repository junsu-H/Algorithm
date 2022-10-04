# BOJ_7576 토마토 G5

from sys import stdin
from collections import deque

input = stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

M, N = map(int, input().rstrip().split())
tomato = [list(map(int, input().rstrip().split())) for _ in range(N)]

q = deque()

# 큐에 시작점 담기
for i in range(N):
	for j in range(M):
		if tomato[i][j] == 1:
			q.append((i,j))

while q:
	x, y = q.popleft()

	for i in range(4):
		nx = x + dx[i]
		ny = y + dy[i]

		# tomato 범위
		if 0 <= nx < N and 0 <= ny < M:
			# 이동할 수 있으면
			if tomato[nx][ny] == 0:
				# 다음 갈 위치 = 현재 위치 + 1
				tomato[nx][ny] = tomato[x][y] + 1
				# 다음 갈 위치 큐에 담기
				q.append((nx, ny))

answer = 0
for t in tomato:
	# 0이 있으면 갈 수 없는 곳
	if 0 in t:
		print(-1)
		exit()
	# 0이 없으면 모든 곳을 감.
	else:
		answer = max(answer, max(t))

# 처음 start가 1이므로 -1
print(answer - 1)