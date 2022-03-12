# BOJ_18312 시각

N, K = map(int, input().split())

answer = 0

for i in range(N+1):
	i = '0' + str(i) if len(str(i)) == 1 else str(i)
	
	for j in range(60):
		j = '0' + str(j) if len(str(j)) == 1 else str(j)

		for k in range(60):
			k = '0' + str(k) if len(str(k)) == 1 else str(k)

			if str(K) in i + j + k:
				answer += 1

print(answer)