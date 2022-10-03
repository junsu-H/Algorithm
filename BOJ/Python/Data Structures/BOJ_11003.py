# BOJ_11003 최솟값 찾기 G1

from sys import stdin
from collections import deque

input = stdin.readline

N, L = map(int, input().rstrip().split())
A = list(map(int, input().rstrip().split()))

q = deque()
answer = [float('inf')] * N

for i in range(N):
	while q:
		a, idx = q[-1][0], q[0][1]

		# 최솟값이 아니면
		if a > A[i]:
			q.pop()
		
		# 범위에 해당하지 않은 값이면 삭제
		elif idx < i - L + 1:
			q.popleft()

		else:
			break
		
	q.append((A[i], i))

	# queue 가장 앞에 있는 것이 최솟값
	answer[i] = q[0][0]

print(*answer)