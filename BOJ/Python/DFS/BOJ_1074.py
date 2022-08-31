# BOJ_1074 Z S1

from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 5)

input = stdin.readline

N, r, c = map(int, input().rstrip().split())
answer = 0

def dfs(n, x, y):
	global answer

	if x == r and y == c:
		print(answer)
		exit(0)

	if n == 1:
		answer += 1
		return

	# r, c가 포함되지 않는다면 n ** 2(N사분면 전체)를 더하면 된다.
	if not (x <= r < x + n and y <= c < y + n):
		answer += n ** 2
		return
	
	m = n//2

	# 4등분하기
	dfs(m, x, y)			# 2사분면
	dfs(m, x, y + m)		# 1사분면
	dfs(m, x + m, y)		# 3사분면
	dfs(m, x + m, y + m)	# 4사분면

dfs(2 ** N, 0, 0)
print(answer)