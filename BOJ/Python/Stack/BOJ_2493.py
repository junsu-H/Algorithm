# BOJ_2493 탑 G5

from sys import stdin

input = stdin.readline

N = int(input().rstrip())

tops = list(map(int, input().rstrip().split()))
stack = []

answer = []

for i in range(N):
	while stack:
		idx, top = stack[-1]
		
		# top이 더 크면 answer에 idx 담기
		if tops[i] < top:
			answer.append(idx)
			break
		
		# 작으면 하나씩 빼고 비교
		else:
			stack.pop()
		
	if not stack:
		answer.append(0)

	stack.append((i+1, tops[i]))

print(*answer)