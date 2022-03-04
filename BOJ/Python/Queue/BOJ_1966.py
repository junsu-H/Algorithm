# BOJ_1966 프린터 큐

from sys import stdin
from collections import deque

input = stdin.readline

T = int(input().rstrip())

for _ in range(T):
    N, M = map(int, input().rstrip().split()) 
    data = list(map(int, input().rstrip().split()))
    queue = deque([(d, i) for i, d in enumerate(data)])
    answer = 0

    while queue:
        max_queue = max(queue)[0]
        d, i = queue.popleft()

        if d == max_queue:
            answer += 1
            if i == M:
                print(answer)
                break
        else:
            queue.append((d, i))