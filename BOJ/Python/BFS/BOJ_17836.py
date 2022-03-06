# BOJ_17836 공주님을 구해라!

from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N, M, T = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
visit = [[0] * M for _ in range(N)]

def bfs():
    queue = deque([(0, 0)])
    answer = float("inf")
    visit[0][0] = 1

    while queue:
        x, y = queue.popleft()


        if graph[x][y] == 2:
            answer = abs(N-1-x) + abs(M-1-y) + visit[x][y] - 1
        
        if (x, y) == (N-1, M-1):
            answer = min(visit[x][y]-1, answer)
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M and visit[nx][ny] == 0:
                if graph[nx][ny] != 1:
                    visit[nx][ny] = visit[x][y] + 1
                    queue.append((nx, ny))
    
    return answer

count = bfs()
if 0 < count <= T:
    print(count)
else:
    print("Fail")