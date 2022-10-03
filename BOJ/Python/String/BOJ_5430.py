# BOJ_5430 AC G5

from sys import stdin
from collections import deque

input = stdin.readline

T = int(input().rstrip())

for _ in range(T):
	reverse_cnt = 0
	is_error = False

	p = input().rstrip()

	n = int(input().rstrip())
	data = deque(input().rstrip()[1:-1].split(","))

	for command in p:
		# 배열을 뒤집어야 할 때
		if command == "R":
			reverse_cnt += 1
		
		# 배열 중 가장 앞 요소를 삭제해야 할 때
		elif command == "D":
			if n == 0:
				is_error = True
				break
			
			# reverse_cnt 짝수면 처음이랑 같으므로 앞에서 삭제
			if reverse_cnt % 2 == 0:
				data.popleft()

			# reverse_cnt 홀수면 뒤집어야 하므로 뒤에서 삭제
			elif reverse_cnt % 2 == 1:
				data.pop()
			
			# 배열 하나가 삭제되므로 -1 해줘야 함.
			n -= 1
				
	if reverse_cnt % 2 == 1:
		data.reverse()
	
	if is_error:
		print("error")
	else:
		print("[" + ",".join(data) + "]")