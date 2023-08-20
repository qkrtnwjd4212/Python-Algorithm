# 백준 1753 - 최단경로
import heapq
import sys 
input = sys.stdin.readline 
INF = int(1e9)

v, e = map(int, input().split()) # 정점(1부터), 간선
K = int(input()) # 시작점
graph = [[] for _ in range(v+1)]
distance = [INF] * (v+1)

for _ in range(e): # 변수 v 똑같은거써서 덮어씌워짐!!
    u, v, w = map(int, input().split()) # u->v 비용이 w
    graph[u].append((v, w))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(K)
# print(v)

for i in range(1, v+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])
    
# for i in distance[1:]:
#     if i == INF:
#         print("INF")
#     else:
#         print(i)
