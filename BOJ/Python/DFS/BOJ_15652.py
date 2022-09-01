# BOJ_15652 N과 M (4)

from sys import setrecursionlimit, stdin

setrecursionlimit(10**5)

input = stdin.readline

N, M = map(int, input().split())
answer = [0] * M

def dfs(depth, number):
	if depth == M:
		print(*answer)
	
	else:
		for i in range(number, N + 1):
			answer[depth] = i
			dfs(depth + 1, i)

dfs(0, 1)