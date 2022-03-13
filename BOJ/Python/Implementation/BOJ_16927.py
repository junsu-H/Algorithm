# BOJ_16927 배열 돌리기 2

from collections import deque

def cycle(x, y, N, M):
	# N, M = 4, 4일 때

	# [0][0], [0][1], [0][2]
	# 상에 있는 M-1개
	for j in range(M-1):
		nx = x
		ny = y + j
		q.append(grid[nx][ny])

	# [0][3], [1][3], [2][3]
	# 우에 있는 N-1개
	for i in range(N-1):
		nx = x + i
		ny = y + M - 1
		q.append(grid[nx][ny])

	# [3][3], [3][2], [3][1]
	# 하에 있는 M-1개
	for j in range(M-1):
		nx = x + N - 1
		ny = y + M - 1 - j
		q.append(grid[nx][ny])

	# [3][0], [2][0], [1][0]
	# 좌에 있는 N-1개
	for i in range(N-1):
		nx = x + N - 1 - i
		ny = y
		q.append(grid[x+N-1-i][ny])

	q.rotate(-R)

	# 상에 있는 M-1개
	for j in range(M-1):
		nx = x
		ny = y + j
		grid[nx][ny] = q.popleft()

	# [0][3], [1][3], [2][3]
	# 우에 있는 N-1개
	for i in range(N-1):
		nx = x + i
		ny = y + M - 1
		grid[nx][ny] = q.popleft()

	# [3][3], [3][2], [3][1]
	# 하에 있는 M-1개
	for j in range(M-1):
		nx = x + N - 1
		ny = y + M - 1 - j
		grid[nx][ny] = q.popleft()

	# [3][0], [2][0], [1][0]
	# 좌에 있는 N-1개
	for i in range(N-1):
		nx = x + N - 1 - i
		ny = y
		grid[nx][ny] = q.popleft()

N, M, R = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

q = deque()
x = y = 0

while True:
	if N == 0 or M == 0: break

	cycle(x, y, N, M)
	x += 1
	y += 1
	N -= 2 
	M -= 2

for g in grid:
	print(*g)