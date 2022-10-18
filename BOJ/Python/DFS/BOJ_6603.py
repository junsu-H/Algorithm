# BOJ_6603 로또 S2

from sys import stdin

input = stdin.readline

def dfs(depth, start):
	# 아래로 6개 내려갔을 때
	if depth == 7:
		print(*answer[1:])
		return
	else:
		for i in range(start, end + 1):
			answer[depth] = lotto[i]
			dfs(depth + 1, i + 1)

while True:
	lotto = list(map(int, input().rstrip().split()))

	end = lotto[0]
	
	if end == 0:
		break
	
	answer = [0] * 7
	dfs(1, 1)
	
	print()