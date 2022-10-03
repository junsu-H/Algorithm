# BOJ_1021 회전하는 큐 S3

from sys import stdin
from collections import deque

input = stdin.readline

N, M = list(map(int, input().rstrip().split()))
data = list(map(int, input().rstrip().split()))

q = deque(list(range(1, N+1)))
answer = 0

for d in data:
	while True:
		idx = q.index(d)
		
		# 찾았으니까 
		if idx == 0:
			q.popleft()
			break
		
		# 왼쪽으로 밀기
		if idx <= len(q) // 2:
			q.rotate(-1)
	
		# 오른쪽으로 밀기
		else:
			q.rotate(1)
		
		answer += 1

print(answer)