# BOJ_5397 키로거 S2

from sys import stdin

input = stdin.readline

T = int(input().rstrip())

for _ in range(T):
	cursor_left = []
	cursor_right = []
	data = input().rstrip()

	for d in data:
		if d not in ("<", ">", "-"):
			cursor_left.append(d)

		# 커서가 왼쪽으로 갈 때
		elif d == "<" and cursor_left:
			cursor_right.append(cursor_left.pop())

		# 커서가 오른쪽으로 갈 때
		elif d == ">" and cursor_right:
			cursor_left.append(cursor_right.pop())

		elif d == "-" and cursor_left:
			cursor_left.pop()
			
	print(''.join(cursor_left) + ''.join(cursor_right[::-1]))