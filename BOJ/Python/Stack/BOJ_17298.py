# BOJ_17298 오큰수 G4

from sys import stdin

input = stdin.readline

N = int(input().rstrip())
seq = list(map(int, input().rstrip().split()))

stack = [0]
answer = [-1] * N

for i in range(1, N):
	# stack에 값이 있고, stack의 가장 위에 있는 값이 
	# seq[index]보다 seq[i] 더 크면 answer 담음.
	while stack and seq[stack[-1]] < seq[i]:
		answer[stack.pop()] = seq[i]
	
	# stack에는 index 담음.
	stack.append(i)

print(*answer)   