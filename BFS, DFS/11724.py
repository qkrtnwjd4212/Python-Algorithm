# 백준 11724 - 연결 요소의 개수

from collections import deque

n, m = map(int, input().split()) # 노드, 링크
graph = [[] for _ in range(n+1)] 
visited = [False] * (n+1) # 방문 표시할 리스트

def bfs(s):
    queue = deque([s])
    visited[s] = True # 방문 처리

    while queue:
        node = queue.popleft() # 큐를 돌면서 현재 노드를 꺼냄
        for i in graph[node]: # 현재 노드와 연결된 노드들을 돌면서
            if not visited[i]: # 방문하지 않았으면 
                visited[i] = True 
                queue.append(i)

# 그래프 생성
for i in range(m):
    x, y = map(int, input().split( ))
    graph[x].append(y)
    graph[y].append(x)

count = 0
for i in range(1, n+1):
    if not visited[i]:
        if not graph[i]: # 연결된 노드가 없음 -> 하나의 연결요소
            visited[i] = True
            count += 1
        else:
            bfs(i)
            count += 1
print(count)
