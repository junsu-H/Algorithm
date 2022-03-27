# BOJ_3040 백설 공주와 일곱 난쟁이

from itertools import combinations

for c in combinations([int(input()) for _ in range(9)], 7):
	if sum(c) == 100:
		print(*c, sep = '\n')