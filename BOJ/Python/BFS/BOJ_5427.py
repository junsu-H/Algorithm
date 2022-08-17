# BOJ_5427 불 G4
# PyPy3

from collections import deque
from sys import stdin

input = stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    global s_q, f_q, answer

    depth = []

    while True:
        answer += 1

        while f_q:
            x, y = f_q.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < h and 0 <= ny < w:
                    if grid[nx][ny] == "." or grid[nx][ny] == "@" or grid[nx][ny] == "V":
                        grid[nx][ny] = '*'
                        depth.append((nx, ny))

        f_q = deque(depth)

        depth.clear()

        while s_q:
            x, y = s_q.popleft()

            if x == 0 or y == 0 or x == h - 1 or y == w - 1:
                return answer

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < h and 0 <= ny < w:
                    if grid[nx][ny] == ".":
                        depth.append((nx, ny))
                        grid[x][y] = "V"
                        grid[nx][ny] = "@"

        s_q = deque(depth)

        if not s_q:
            return False


T = int(input().rstrip())

for _ in range(T):
    f_q = deque()
    s_q = deque()
    answer = 0

    w, h = map(int, input().rstrip().split())
    grid = [list(map(str, input().rstrip())) for _ in range(h)]

    for i in range(h):
        for j in range(w):
            if grid[i][j] == "@":
                s_q.append((i, j))
            if grid[i][j] == "*":
                f_q.append((i, j))
    if bfs():
        print(answer)
    else:
        print("IMPOSSIBLE")