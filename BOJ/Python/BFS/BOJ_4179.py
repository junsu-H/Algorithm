# BOJ_4179 불! G4

from sys import stdin
from collections import deque

input = stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

R, C = map(int, input().rstrip().split())
maze = [list(map(str, input().rstrip())) for _ in range(R)]

jihoon_q = deque()
fire_q = deque()

for i in range(R):
    for j in range(C):
        if maze[i][j] == "J": jihoon_q.append((i, j))
        elif maze[i][j] == "F": fire_q.append((i, j))

depth = []
answer = 0

while True:
	# 1분씩 더하기
	answer += 1

	# 불 먼저
	while fire_q:
		x, y = fire_q.popleft()

		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]

			if 0 <= nx < R and 0 <= ny < C:
				if maze[nx][ny] == "." or maze[nx][ny] == "V":
					# maze.append((nx, ny)) 하면 매 분 한 칸씩 가는 걸 확인 못 함.
					depth.append((nx, ny))
					maze[nx][ny] = "F"

	# 1분 후 fire_q
	fire_q = deque(depth)
	depth.clear()

	# 그 다음에 지훈
	while jihoon_q:
		x, y = jihoon_q.popleft()

		if x == 0 or y == 0 or x == R - 1 or y == C - 1:
			print(answer)
			exit()

		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]

			if 0 <= nx < R and 0 <= ny < C:
				if maze[nx][ny] == ".":
					# maze.append((nx, ny)) 하면 매 분 한 칸씩 가는 걸 확인 못 함.
					depth.append((nx, ny))
					maze[x][y] = "V"
					maze[nx][ny] = "J"

	# 1분 후 jihoon_q
	jihoon_q = deque(depth)

	if not jihoon_q:
		print("IMPOSSIBLE")
		exit()