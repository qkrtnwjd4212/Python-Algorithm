# 백준 18352 - 특정 도시의 거리 찾기
import sys 
from collections import deque
input = sys.stdin.readline 

n, m, k, x = map(int, input().rstrip().split()) # 도시, 도로, 찾을 값, 출발점
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1) 
dist = [0] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

def bfs(s):
    queue = deque([s])
    visited[s] = True 

    while queue:
        node = queue.popleft() 
        for i in graph[node]: 
            if not visited[i]:
                visited[i] = True
                dist[i] = dist[node] + 1
                queue.append(i)

bfs(x)
count = []
for i in range(len(dist)):
    if dist[i] == k:
        count.append(i)
count.sort()

if not count:
    print(-1)
else:
    for node in count:
        print(node)