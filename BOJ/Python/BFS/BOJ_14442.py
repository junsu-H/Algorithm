# BOJ_14442 벽 부수고 이동하기 2 G3
# PyPy3
# hint 3차원

from sys import stdin
from collections import deque

input = stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N, M, K = map(int, input().rstrip().split())
grid = [list(map(int, input().rstrip())) for _ in range(N)]

visited = [[[0]*(K + 1) for _ in range(M)]  for _ in range(N)]
visited[0][0][K] = 1

q = deque([(0, 0, K)])

while q:
	x, y, z = q.popleft()

	if x == N - 1 and y == M - 1:
		print(visited[x][y][z])
		break

	for i in range(4):
		nx = x + dx[i]
		ny = y + dy[i]

		if 0 <= nx < N and 0 <= ny < M:
			# 벽 안 부수고
			if grid[nx][ny] == 0 and visited[nx][ny][z] == 0:
				q.append((nx, ny, z))
				visited[nx][ny][z] = visited[x][y][z] + 1
			
			# 벽 부수고
			elif grid[nx][ny] == 1 and visited[nx][ny][z-1] == 0 and z > 0:
				q.append((nx, ny, z-1))
				visited[nx][ny][z-1] = visited[x][y][z] + 1

else:
	print(-1)