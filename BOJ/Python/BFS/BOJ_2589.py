# BOJ_2589 보물섬
# PyPy3

from collections import deque

N, M = map(int, input().split())
grid = [list(input()) for _ in range(N)]
answer = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(i, j):
    q = deque([(i, j)])
    visit = [[0] * M for _ in range(N)]
    visit[i][j] = 1
    cnt = 0

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M and grid[nx][ny] == "L" and visit[nx][ny] == 0:
                visit[nx][ny] = visit[x][y] + 1
                cnt = max(cnt, visit[nx][ny])
                q.append((nx, ny))

    return cnt - 1 # 마지막은 경로가 아니므로 -1 해야 됨


for i in range(N):
    for j in range(M):
        if grid[i][j] == "L":
            answer = max(answer, bfs(i, j))

print(answer)
