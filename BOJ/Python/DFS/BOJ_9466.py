# BOJ_9466 텀 프로젝트 G3
# hint: cycle dfs

from sys import stdin, setrecursionlimit

ipnut = stdin.readline
setrecursionlimit(10**6)

T = int(input().rstrip())

def dfs(idx):
	global cnt
	visited[idx] = 1

	ni = graph[idx]				# 다음 방문할 곳
	
	if visited[ni] == 0:		# 방문 안 했다면
		dfs(ni)

	else:						# 방문했다면
		if ni not in cycle:		# 사이클에 포함되어 있지 않다면
			cnt += 1 			# 자기 자신 +1
			
			while ni != idx: 	# 자기 자신이 아닐 때까지
				cnt += 1 		# 자기와 이어진 학생들 더하기
				ni = graph[ni] 	# 다음 학생

	cycle.add(idx)

for _ in range(T):
	N = int(input().rstrip())
	graph = [0] + list(map(int, input().rstrip().split()))
	visited = [0] * (N+1)
	cycle = set()

	cnt = 0
	for idx in range(1, N+1):
		if not visited[idx]:
			dfs(idx)

	print(N - cnt)