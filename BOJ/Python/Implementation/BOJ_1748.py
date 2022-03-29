# BOJ_1748 수 이어 쓰기 1

N = input()
length = len(N) - 1
answer = 0

for i in range(length):
    answer += 9 * (10**i) * (i+1)
    
answer += (int(N)-(10 ** length)+1) * (length+1)

print(answer)