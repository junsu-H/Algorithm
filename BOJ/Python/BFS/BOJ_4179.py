# BOJ_4179 불! G4

from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

R, C = map(int, input().split())
maze = [list(map(str, input())) for _ in range(R)]

j_q = deque()
f_q = deque()
answer = 0

for i in range(R):
    for j in range(C):
        if maze[i][j] == "J":
            j_q.append((i, j))
        if maze[i][j] == "F":
            f_q.append((i, j))


def bfs():
    global j_q, f_q, answer

    depth = []

    while True:
        answer += 1

        while f_q:
            x, y, = f_q.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < R and 0 <= ny < C:
                    if maze[nx][ny] == "." or maze[nx][ny] == "V":
                        # maze.append((nx, ny)) 하면 매 분 한 칸씩 가는 걸 확인 못 함.
                        depth.append((nx, ny))
                        maze[nx][ny] = "F"

        # 매 분 후 f_q
        f_q = deque(depth)

        depth.clear()
        while j_q:
            x, y, = j_q.popleft()

            if x == 0 or y == 0 or x == R - 1 or y == C - 1:
                return answer

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < R and 0 <= ny < C:
                    if maze[nx][ny] == ".":
                        # maze.append((nx, ny)) 하면 매 분 한 칸씩 가는 걸 확인 못 함.
                        depth.append((nx, ny))
                        maze[x][y] = "V"
                        maze[nx][ny] = "J"

        # 매 분 후 j_q
        j_q = deque(depth)

        if not j_q:
            return False


if bfs():
    print(answer)
else:
    print("IMPOSSIBLE")