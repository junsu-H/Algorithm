# BOJ_9663 N-Queen

from sys import setrecursionlimit, stdin

setrecursionlimit(10 ** 5)
input = stdin.readline

def is_promising(row):
    for i in range(row):
          if queen[row] == queen[i] or abs(queen[row] - queen[i]) == row - i:
            return False
    return True

def dfs(row):
	global answer

	if row == N:
		answer += 1
		return
	
	else:
		for col in range(N):
			queen[row] = col

			if is_promising(row):
				dfs(row + 1)
			else:
				continue

N = int(input().rstrip())
queen = [0] * N
answer = 0

dfs(0)
print(answer)