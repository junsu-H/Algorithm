# BOJ_5014 스타트링크 G5

from sys import stdin
from collections import deque

input = stdin.readline

F, S, G, U, D = map(int, input().rstrip().split())

visited = [0] * (F+1)
visited[S] = 1 

q = deque([S])

while q:
	current = q.popleft()

	if current == G:
		print(visited[G] - 1) # 2 1 1 1 0 이 케이스 때문에 visited[S] = 1 하고 -1

	up = current + U
	down = current - D

	for next in (up, down):
		if 0 < next <= F and visited[next] == 0:
			visited[next] = visited[current] + 1
			q.append(next)

if visited[G] == 0:
	print("use the stairs")