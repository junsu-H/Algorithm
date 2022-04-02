# BOJ_2583 영역 구하기

N, M, K = map(int, input().split())
grid = [[1] * M for _ in range(N)]

for _ in range(K):
	x1, y1, x2, y2  = map(int, input().split())

	for i in range(x1, x2):
		for j in range(y1, y2):
			grid[j][i] = 0

from collections import deque

answer = []
visit = [[0] * M for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(i, j):
	cnt = 1
	q = deque([(i, j)])

	while q:
		x, y = q.popleft()

		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]

			if 0 <= nx < N and 0 <= ny < M and visit[nx][ny] == 0 and grid[nx][ny] == 1:
				visit[nx][ny] = 1
				grid[nx][ny] = -1
				cnt += 1
				q.append((nx, ny))
	
	return cnt

for i in range(N):
	for j in range(M):
		if grid[i][j] == 1:
			grid[i][j] = -1
			answer.append(bfs(i,j))

print(len(answer))
print(*sorted(answer))