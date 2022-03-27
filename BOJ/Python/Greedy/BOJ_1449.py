# BOJ_1449 수리공 항승

N, L = map(int, input().split())

tapes = sorted(list(map(int, input().split())))

start = 0
count = 0

for tape in tapes:
	if start < tape:
		start = tape + L - 1
		count += 1

print(count)