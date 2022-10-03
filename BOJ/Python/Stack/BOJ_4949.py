# BOJ_4949 균형잡힌 세상 S4

from sys import stdin

input = stdin.readline

bracket = {
	")": "(",
	"]": "[",
}

while True:
	string = input().rstrip()
	
	if string == ".":
		break

	is_balance = True
	stack = []

	for s in string:
		if s in ("(", "["):
			stack.append(s)
		
		elif s in (")", "]"):
			if len(stack) == 0:
				is_balance = False
				break

			if bracket[s] == stack[-1]:
				stack.pop()
			else:
				is_balance = False
				break
		
	if is_balance and len(stack) == 0:
		print("yes")
	else:
		print("no")