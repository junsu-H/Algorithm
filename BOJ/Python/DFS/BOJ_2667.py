# BOJ_2667 단지번호붙이기

from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 9)

input = stdin.readline

def dfs(x, y):
    global count

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False
    
    if home_map[x][y] == 1:
        home_map[x][y] = 0 
        count += 1
        
        # 상, 하, 좌, 우
        dfs(x + dx[0], y + dy[0])
        dfs(x + dx[1], y + dy[1])
        dfs(x + dx[2], y + dy[2])
        dfs(x + dx[3], y + dy[3])
        return count

n = int(input().rstrip())

home_map = [list(map(int, input().rstrip())) for _ in range(n)]
answer = []
count = 0

for i in range(n):
    for j in range(n):
        if home_map[i][j] == 1:
            count = 0
            answer.append(dfs(i, j))

answer.sort()

print(len(answer))

for a in answer:
    print(a)