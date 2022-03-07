# BOJ_7562 나이트의 이동

from collections import deque

dx = [-1, -2, -2, -1, 1, 2, 2, 1]
dy = [-2, -1, 1, 2, 2, 1, -1, -2]

def bfs(cur_x, cur_y, next_x, next_y):
    queue = deque([(cur_x, cur_y)])

    while queue:
        x, y = queue.popleft()

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < L and 0 <= ny < L and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1

                if (nx, ny) == (next_x, next_y):
                    print(graph[nx][ny])
                    return
              
                queue.append((nx, ny))

T = int(input())

for _ in range(T):
    L = int(input())

    graph = [[0] * L for _ in range(L)]
    
    cur_x, cur_y = map(int, input().split())
    next_x, next_y = map(int, input().split())
    
    if (cur_x, cur_y) == (next_x, next_y):
        print(0)
    else:
        bfs(cur_x, cur_y, next_x, next_y)