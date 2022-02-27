# BOJ_1697 숨바꼭질

from collections import deque

N, K = map(int, input().split())

max_idx = 100_001
visit = [0] *  max_idx
queue = deque([(N, 0)])

def bfs():
    while queue:
        value, level = queue.popleft()
        visit[value] = 1

        if value == K:
            return level
        
        level += 1
        for i in range(1, 4):
            if i == 1: 
                nv = value - 1
            elif i == 2: 
                nv = value + 1
            elif i == 3: 
                nv = value * 2
        
            if 0 <= nv < max_idx and visit[nv] == 0:
                visit[nv] = 1
                queue.append((nv, level))
    
    return level

print(bfs())