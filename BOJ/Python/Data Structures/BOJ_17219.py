# BOJ_17219 비밀번호 찾기 S4

from sys import stdin

input = stdin.readline

N, M = map(int, input().rstrip().split())

sites = dict()

for _ in range(N):
	site, password = map(str, input().rstrip().split())
	sites[site] = password

for _ in range(M):
	site = input().rstrip()
	print(sites[site])