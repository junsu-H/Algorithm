# BOJ_2178 미로 탐색 S1

from sys import stdin
from collections import deque

input = stdin.readline

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N, M = map(int, input().rstrip().split())

grid = [list(map(int, input().rstrip())) for _ in range(N)]

q = deque([(0, 0)])

while q:
    x, y = q.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < M:
            if grid[nx][ny] == 1:
                grid[nx][ny] = 1 + grid[x][y]
                q.append((nx, ny))
    
print(grid[N-1][M-1])