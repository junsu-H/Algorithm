# BOJ_11328 Strfry B2

from sys import stdin

input = stdin.readline

N = int(input())

for _ in range(N):
	first, second = map(str, input().rstrip().split())
	
	first = sorted(first)
	second = sorted(second)

	if (first == second):
		print("Possible")
	else:
		print("Impossible")