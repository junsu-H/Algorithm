# BOJ_2468 안전 영역 S1

from sys import stdin
from collections import deque

input = stdin.readline

N = int(input().rstrip())
area = [list(map(int, input().rstrip().split())) for _ in range(N)]

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(i, j, h):
	q = deque([(i, j, h)])
	visited[i][j] = 1

	while q:
		x, y, h = q.popleft()

		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]	

			if 0 <= nx < N and 0 <= ny < N:
				# 다음에 갈 곳이 h보다 높고, 방문하지 않았다면
				if area[nx][ny] > h and visited[nx][ny] == 0:
					visited[nx][ny] = 1
					q.append((nx, ny, h))

end = 0
for a in area:
	end = max(end, *a)

answer = 0
for h in range(end):
	visited = [[0] * N for _ in range(N)]
	cnt = 0

	for i in range(N):
		for j in range(N):
			# 현재 있는 곳의 높이가 h보다 높고, 방문하지 않았다면
			if area[i][j] > h and visited[i][j] == 0:
				bfs(i, j, h)
				# 안전한 영역 개수 구하기
				cnt += 1

	answer = max(answer, cnt)

print(answer)