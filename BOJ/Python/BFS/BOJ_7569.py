# BOJ_7569 토마토

from collections import deque

# 상하좌우 윗층 아래층
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]
queue = deque(())

def bfs():
    global answer

    while queue:
        z, x, y = queue.popleft()

        for i in range(6):
            nz = z + dz[i]
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nz < H and 0 <= nx < N and 0 <= ny < M:
                if tomato[nz][nx][ny] == 0 and visit[nz][nx][ny] == 0:
                    visit[nz][nx][ny] = visit[z][x][y] + 1
                    tomato[nz][nx][ny] = -1
                    queue.append((nz, nx, ny))
    
M, N, H = map(int, input().split())
tomato = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
visit = [[[0] * M for _ in range(N)] for _ in range(H)]
answer = 0

for k in range(H):
    for i in range(N):
        for j in range(M):
            if tomato[k][i][j] == 1:
                queue.append((k, i, j))

bfs()                

for k in range(H):
    for i in range(N):
        for j in range(M):
            if tomato[k][i][j] == 0:
                print(-1)
                exit()
            else:   
                if visit[k][i][j] > answer:
                    answer = visit[k][i][j]

print(answer)