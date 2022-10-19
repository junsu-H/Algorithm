# BOJ_1759 암호 만들기 G5

from sys import stdin

input = stdin.readline

L, C = map(int, input().rstrip().split())
data = sorted(list(map(str, input().rstrip().split())))

vowels = set('aeiou')
answer = [0] * L
def dfs(depth, start):
	if depth == L:
		set_answer = set(answer)
		# 자음 정보만 남기기
		consonant_only = set_answer - vowels
		# 모음 정보만 남기기
		vowel_only = set_answer & vowels
		
		# 모음 1개 이상 and 자음 2개 이상
		if len(vowel_only) >= 1 and len(consonant_only) >= 2:
			for a in answer:
				print(a, end='')
			print()
			return

	else:
		for i in range(start, C):
			answer[depth] = data[i]
			dfs(depth + 1, i + 1)
	
dfs(0, 0)