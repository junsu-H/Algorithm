# BOJ_1600 말이 되고픈 원숭이 G3
# hint: 선택지가 하나 더 있으면 3차원

from collections import deque
from sys import stdin

input = stdin.readline

# 원숭이 이동
monkey_dx = [-1, 1, 0, 0]
monkey_dy = [0, 0, -1, 1]

# 말 이동
horse_dx = [-1, -2, -2, -1, 1, 2, 2, 1]
horse_dy = [-2, -1, 1, 2, 2, 1, -1, -2]

K = int(input().rstrip())
W, H = map(int, input().rstrip().split())

grid = [list(map(int, input().rstrip().split())) for _ in range(H)]

visited = [[[0] * (K + 1) for _ in range(W)] for _ in range(H)]


def check(nx, ny, cnt):
    if 0 <= nx < H and 0 <= ny < W:
        if grid[nx][ny] == 0 and visited[nx][ny][cnt] == 0:
            return True

    return False


def bfs():
    q = deque([(0, 0, 0)])

    while q:
        x, y, cnt = q.popleft()

        if x == H - 1 and y == W - 1:
            return visited[x][y][cnt]

        for i in range(4):
            mx = x + monkey_dx[i]
            my = y + monkey_dy[i]

            if check(mx, my, cnt):
                q.append((mx, my, cnt))
                visited[mx][my][cnt] = visited[x][y][cnt] + 1

        if cnt < K:
            for i in range(8):
                hx = x + horse_dx[i]
                hy = y + horse_dy[i]

                if check(hx, hy, cnt + 1):
                    q.append((hx, hy, cnt + 1))
                    visited[hx][hy][cnt + 1] = visited[x][y][cnt] + 1

    return -1


print(bfs())