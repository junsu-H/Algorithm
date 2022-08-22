# BOJ_16933 벽 부수고 이동하기 3 G1
# PyPy3 

from sys import stdin
from collections import deque

input = stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N, M, K = map(int, input().rstrip().split())

grid = [list(map(int, input().rstrip())) for _ in range(N)]
visited = [[[0]*(K+1) for _ in range(M)] for _ in range(N)]
visited[0][0][0] = 1

def check(nx, ny, nz):
	return 0 <= nx < N and 0 <= ny < M and visited[nx][ny][nz] == 0

def bfs():
	q = deque([(0, 0, 0)])

	day = 1

	while q:
		if day > 0: night = False
		else: night = True

		for _ in range(len(q)):
			x, y, z = q.popleft()
			today = abs(day)

			if x == N - 1 and y == M - 1:
				return today

			for i in range(4):
				nx = x + dx[i]
				ny = y + dy[i]
				
				if check(nx, ny, z):
					# 벽이 아닐 때
					if grid[nx][ny] == 0:
						q.append((nx, ny, z))
						visited[nx][ny][z] = today + 1
					
					# 벽일 때
					elif K > z and visited[nx][ny][z+1] == 0:
						# 가만히
						if night:
							q.append((x, y, z))
						# 벽 부수고
						else:
							q.append((nx, ny, z + 1))
							visited[nx][ny][z + 1] = today + 1
			
		if day > 0: day += 1
		else: day -= 1
		
		day *= -1

	return -1

print(bfs())