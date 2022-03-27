# BOJ_1987 알파벳

R, C = map(int, input().split())
board = [list(input()) for _ in range(R)]

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

alphas = set(board[0][0])
answer = 1

def dfs(x, y, cnt):
	global answer
	
	if answer < cnt:
		answer = cnt

	for i in range(4):
		nx = x + dx[i]
		ny = y + dy[i]

		if 0 <= nx < R and 0 <= ny < C and board[nx][ny] not in alphas:
			alphas.add(board[nx][ny])
			dfs(nx, ny, cnt + 1)
			alphas.remove(board[nx][ny])

dfs(0, 0, answer)
print(answer)