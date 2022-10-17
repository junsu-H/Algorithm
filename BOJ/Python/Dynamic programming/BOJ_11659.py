# BOJ_11659 구간 합 구하기 4 S3

from sys import stdin

input = stdin.readline

N, M = map(int, input().rstrip().split())
data = [0] + list(map(int, input().rstrip().split()))
dp = [0] * 100_001

for i in range(1, N + 1):
	dp[i] = dp[i-1] + data[i] 

for _ in range(M):
	i, j = map(int, input().rstrip().split())
	print(dp[j] - dp[i-1])