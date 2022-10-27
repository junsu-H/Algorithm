# BOJ_1351 무한 수열 G5

from collections import defaultdict
from sys import stdin

input = stdin.readline

N, P, G = map(int, input().rstrip().split())

dp = defaultdict(int)
dp[0] = 1 
def dfs(i):
	# 값이 있으면
	if dp[i]:
		return dp[i]

	dp[i] = dfs(i // P) + dfs(i // G)
	return dp[i]

print(dfs(N))