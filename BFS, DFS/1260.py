# 백준 1260 - DFS와 BFS
from collections import deque
import sys 
input = sys.stdin.readline
sys.setrecursionlimit(10000) 

n, m, v = map(int, input().split()) # 노드, 링크, 시작번호
graph = [[] for _ in range(n+1)] 
visited1 = [False] * (n+1) 
visited2 = [False] * (n+1) 

def bfs(s):
    queue = deque([s])
    visited1[s] = True

    while queue:
        node = queue.popleft() # 큐를 돌면서 현재 노드를 꺼냄
        print(node, end=' ')
        for i in graph[node]:
            if not visited1[i]:
                visited1[i] = True 
                queue.append(i)

def dfs(s):
    visited2[s] = True
    print(s, end=' ')
    for i in graph[s]:
       if not visited2[i]:
           dfs(i)

for _ in range(m):
    x, y = map(int, input().rstrip().split())
    graph[x].append(y)
    graph[y].append(x)

for i in range(n+1): # N이 아니라 N+1!!!!!!
    graph[i].sort() # 노드 번호 정렬!!!

dfs(v)
print()
bfs(v)