# 미로 탐색

from collections import deque

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N, M = map(int, input().split())

grid = [list(map(int, input())) for _ in range(N)]

queue = deque([(0, 0)])

def bfs(grid):
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M and grid[nx][ny] == 1:
                grid[nx][ny] = 1 + grid[x][y]
                queue.append((nx, ny))
    
    return grid[N-1][M-1]

print(bfs(grid))