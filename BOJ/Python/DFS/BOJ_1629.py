# BOJ_1629 곱셈 S1
# hint (A^B) % C == ((A^(B-x)) % C * (A^x) % C) % C

from sys import stdin, setrecursionlimit

input = stdin.readline

setrecursionlimit(10**5)

A, B, C = map(int, input().rstrip().split())

def dfs(result, n):
	if n == 1:
		return result % C

	else:
		case = dfs(result, n // 2)

		if n % 2 == 0:
			return (case * case) % C
		else:
			return (case * case * result) % C

print(dfs(A, B))