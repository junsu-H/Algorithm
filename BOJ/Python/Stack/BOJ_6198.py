# BOJ_6198 옥상 정원 꾸미기 G5

from sys import stdin

input = stdin.readline

N = int(input().rstrip())

buildings = [int(input().rstrip()) for _ in range(N)]

stack = []
answer = 0

for i in range(N):
	while stack and stack[-1] <= buildings[i]:
		stack.pop()
	
	stack.append(buildings[i])
	
	answer += len(stack) - 1

print(answer)