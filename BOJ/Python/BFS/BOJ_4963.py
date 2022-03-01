# BOJ_4963 섬의 개수

from collections import deque

# 상/하/좌/우/좌상/좌하/우상/우하
dx = [-1, 1, 0, 0, -1, 1, -1, 1]
dy = [0, 0, -1, 1, -1, -1, 1, 1]

def bfs(i, j):
    queue = deque([(i, j)])

    while queue:
        x, y = queue.popleft()
        
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < h and 0 <= ny < w and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))

while True:
    w, h = map(int, input().split())
    if w == h == 0:
        break
    
    answer = 0
    graph = [list(map(int, input().split())) for _ in range(h)]

    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                bfs(i, j)
                answer += 1

    print(answer)