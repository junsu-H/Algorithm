# BOJ_1743 음식물 피하기

from collections import deque

N, M, K = map(int, input().split())

grid = [[0] * M for _ in range(N)]
visit = [[0] * M for _ in range(N)]

for _ in range(K):
	x, y = map(int, input().split())
	grid[x-1][y-1] = 1

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(i, j):
	q = deque([(i,j)])
	grid[i][j] = -1
	res = 1
	
	while q:
		x, y = q.popleft()

		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]

			if 0 <= nx < N and 0 <= ny < M and grid[nx][ny] == 1:
					grid[nx][ny] = -1			
					res += 1
					q.append((nx, ny))
	return res

answer = 0
for i in range(N):
	for j in range(M):
		if grid[i][j] == 1:
			answer = max(answer, bfs(i, j))

print(answer)