# BOJ_10026 적록색약

from collections import deque

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(i, j, color):
    queue = deque([(i,j)])
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] == color and visit[nx][ny] == 0:
                visit[nx][ny] = 1
                queue.append((nx, ny))

N = int(input())
graph = [list(input()) for _ in range(N)]
visit = [[0] * N for _ in range(N)]
count = 0

# 색약 아닐 때
for i in range(N):
    for j in range(N):
        if visit[i][j] == 0:
            bfs(i, j, graph[i][j])
            count += 1

print(count, end = ' ')

# 색약일 때
for i in range(N):
    for j in range(N):
        if graph[i][j] == 'G':
            graph[i][j] = 'R'

visit = [[0] * N for _ in range(N)]
count = 0       
for i in range(N):
    for j in range(N):
        if visit[i][j] == 0:
            bfs(i, j, graph[i][j])
            count += 1
        
print(count)