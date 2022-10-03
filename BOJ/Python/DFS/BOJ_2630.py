# BOJ_2630 색종이 만들기 S2

from sys import stdin

input = stdin.readline

N = int(input().rstrip())

grid = [list(map(int, input().rstrip().split())) for _ in range(N)]
answer = []

def dfs(x, y, n):
	color = grid[x][y]

	for i in range(x, x+n):
		for j in range(y, y+n):
			if color != grid[i][j]:
				parse = n//2
				dfs(x, y, parse)
				dfs(x, y + parse, parse)
				dfs(x + parse, y, parse)
				dfs(x + parse, y + parse, parse)
				return
	
	if color == 0:
		answer.append(0)
	else:
		answer.append(1)

dfs(0, 0, N)
print(answer.count(0))
print(answer.count(1))