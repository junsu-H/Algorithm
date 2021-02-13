import sys
import heapq

def solution():
    n = int(sys.stdin.readline().rstrip())
    
    answer = 0

    array = []
    for _ in range(n):
        array.append(int(sys.stdin.readline().rstrip()))
    
    heapq.heapify(array)
    while len(array)>1:
        card_sum = heapq.heappop(array) + heapq.heappop(array)
        heapq.heappush(array, card_sum)
        answer += card_sum

    print(answer)

solution()