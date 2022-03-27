# BOJ_1931 회의실 배정

N = int(input())

data = sorted([list(map(int, input().split())) for _ in range(N)], key = lambda x: (x[1], x[0]))

temp = 0
answer = 0

for start, end in data:
	if temp <= start:
		temp = end
		answer += 1

print(answer)