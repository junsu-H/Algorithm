# BOJ_1914 하노이 탑 S1
# hint: 호출의 의미 / 그 호출과 재귀호출의 관계 파악하면 됨.

from sys import setrecursionlimit, stdin

setrecursionlimit(10 ** 5)
input = stdin.readline

N = int(input().rstrip())

def dfs(n, one, two, three):
	if n == 1:
		print(one, three)
		return
	
	# one에서 three를 거쳐 two로 이동
	dfs(n-1, one, three, two)
	
	print(one, three)

	# two에서 one을 거쳐 three로 이동
	dfs(n-1, two, one, three)

# x = 2^N - 1
print(2 ** N - 1)
if N <= 20:
	dfs(N, 1, 2, 3)
