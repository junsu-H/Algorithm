# BOJ_10773 제로 S4

from sys import stdin

input = stdin.readline

K = int(input().rstrip())

stack = []

for _ in range(K):
	num = int(input().rstrip())

	if num != 0:
		stack.append(num)
	elif num == 0 and stack:
		stack.pop()

print(sum(stack))