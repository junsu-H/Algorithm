# BOJ_15657 N과 M (8) S3

from sys import setrecursionlimit, stdin

setrecursionlimit(10**5)

input = stdin.readline

def dfs(depth, start):
	if depth == M:
		print(*answer)

	else:
		for i in range(start, N+1):
			answer[depth] = data[i]
			dfs(depth + 1, i)

N, M = map(int, input().split())
data = [0] + sorted(list(map(int, input().split())))

answer = [0] * M

dfs(0, 1)