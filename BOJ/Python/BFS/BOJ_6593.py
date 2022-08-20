# BOJ_6593 상범 빌딩 G5
# hint 3차원

from sys import stdin
from collections import deque

input = stdin.readline

# 2차원 상하좌우, 3차원 위/아래
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

def bfs():
	while q:
		z, x, y= q.popleft()

		for i in range(6):
			nz = z + dz[i]
			nx = x + dx[i]
			ny = y + dy[i]

			if 0 <= nz < L and 0 <= nx < R and 0 <= ny < C:
				if building[nz][nx][ny] == 0:
					building[nz][nx][ny] = building[z][x][y] + 1
					q.append((nz, nx, ny))

while True:
	q = deque()

	L, R, C = map(int, input().rstrip().split())
	
	if L + R + C == 0:
		break
	
	building = [[[0] * R] for _ in range(L)]

	for l in range(L):
		building[l]=[list(map(str,input().rstrip())) for _ in range(R)]
		input().rstrip()

	for k in range(L):
		for i in range(R):
			for j in range(C):
				if building[k][i][j] == 'S':
					building[k][i][j] = 0
					q.append((k,i,j))
				
				if building[k][i][j] == '.':
					building[k][i][j] = 0

				if building[k][i][j] == 'E':
					building[k][i][j] = 0
					ez, ex, ey = k, i, j
	
	bfs()
	answer = building[ez][ex][ey]
	
	if answer:
		print(f"Escaped in {answer} minute(s).")
	else:
		print("Trapped!")
