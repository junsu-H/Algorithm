# BOJ_1049 기타줄

N, M = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(M)]
PACK = 6

six, _ = sorted(data, key = lambda x: x[0])[0]
_, one = sorted(data, key = lambda x: x[1])[0]

answer = min(one * N, six * (N // PACK) + one * (N % PACK), six * (N // PACK + 1))

print(answer)