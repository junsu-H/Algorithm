# BOJ_2206 벽 부수고 이동하기 G4
# hint 3차원 

from sys import stdin
from collections import deque

input = stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N, M = map(int, input().rstrip().split())
graph = [list(map(int, input().rstrip())) for _ in range(N)]

def bfs():
    queue = deque([(0, 0, 1)])
	# 벽을 부순 케이스[0], 벽을 안 부순 케이스[1]를 3차원으로 표시
    visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
    # 벽을 부술 수 있는 상태
    visited[0][0][1] = 1

    while queue:
        # wall의 개수만큼 벽을 부술 수 있음. 1이면 벽 하나를 부술 수 있음.
        x, y, wall = queue.popleft()
		# 마지막에 도달했을 때 탈출
        if x == N-1 and y == M-1:
            return visited[x][y][wall]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M :
				# 해당 위치로 이동 가능하고, 아직 방문하지 않았다면
                if graph[nx][ny] == 0 and visited[nx][ny][wall] == 0:
                    visited[nx][ny][wall] = visited[x][y][wall] + 1
                    queue.append((nx, ny, wall))

				# 해당 위치가 벽이고, 벽을 부수고 이동
                if graph[nx][ny] == 1 and wall == 1:
                    # 벽을 못 부순 dis = 벽을 부순 dis + 1
                    visited[nx][ny][0] = visited[x][y][1] + 1
                    # 이제부터 벽은 못 부숨
                    queue.append((nx, ny, 0))
    
    return -1

print(bfs())