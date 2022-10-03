# BOJ_1715 카드 정렬하기 G4

from sys import stdin
from heapq import heapify, heappush, heappop

input = stdin.readline()

N = int(input().rstrip())
heap = []

answer = 0

for _ in range(N):
	heap.append(int(input().rstrip()))

	# 최소힙
	heapify(heap)
	
	while len(heap) > 1:
		card_sum = heappop(heap) + heappop(heap)
		heappush(heap, card_sum)

		answer += card_sum

print(answer)