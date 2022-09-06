# BOJ_1753 최단경로 G4
# hint: heap에 넣을 땐 (가중치, 노드) 형태로 넣어야 된다.

from sys import stdin, maxsize
from heapq import heappop, heappush

input = stdin.readline
INF = maxsize

# 정점 개수, 간선 개수
V, E = map(int, input().rstrip().split())

# 시작 정점
K = int(input().rstrip())

d = [INF] * (V+1)
graph = [[] for _ in range(V+1)]

heap = []

def dijkstra(start):
	d[start] = 0

	# heap, (가중치, 노드)
	heappush(heap, (0, start))

	while heap:
		weight, node = heappop(heap)

		# heap에서 뽑은 거리가 테이블에 저장된 거리보다 크면 무시
		if d[node] < weight: continue

		for wei, next_node in graph[node]:
			next_weight = wei + weight

			if next_weight < d[next_node]:
				d[next_node] = next_weight
				heappush(heap, (next_weight, next_node))

for _ in range(E):
	u, v, w = map(int, input().rstrip().split())

	# (가중치, 노드) 
	graph[u].append((w, v))

dijkstra(K)

for i in range(1, V+1):
	if d[i] == INF:	
		print("INF")
	else:
		print(d[i])