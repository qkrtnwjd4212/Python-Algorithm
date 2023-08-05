# 백준 2606 - 바이러스
import sys 
sys.setrecursionlimit(10000) 

n = int(input()) # 컴퓨터 수
m = int(input()) # 연결 쌍 수
visited = [0] * n+1

graph = [[]*n for i in range(n+1)]
for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

count = 0
def dfs(s):
    visited[s] = 1
    for i in graph[s]:
        if visited[i] == 0:
            dfs(i)
            count += 1

dfs(1)
print(count)