# BOJ_1182 부분수열의 합

from sys import setrecursionlimit

setrecursionlimit(10**5)

N, S = map(int, input().split())

data = list(map(int, input().split()))
answer = 0

def dfs(level, hap):
    global answer

    if level >= N:
        return

    hap += data[level]

    if hap == S:
        answer += 1

    dfs(level + 1, hap - data[level])
    dfs(level + 1, hap)

dfs(0, 0)
print(answer)