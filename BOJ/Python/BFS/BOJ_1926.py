# BOJ_1926 그림 S1

from collections import deque

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

answer = []

def bfs(pi, pj):
    q = deque([(pi, pj)])
    grid[pi][pj] = 0
    cnt = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if grid[nx][ny] == 1:
                    grid[nx][ny] = 0
                    q.append((nx, ny))
                    cnt += 1
    answer.append(cnt)

for i in range(n):
    for j in range(m):
        if grid[i][j] == 1:
            bfs(i, j)

if answer:
    print(len(answer))
    print(max(answer))
else:
    print(0)
    print(0)