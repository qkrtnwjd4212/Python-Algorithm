# 백준 2606 - 바이러스
import sys 
input = sys.stdin.readline
sys.setrecursionlimit(10000) # 재귀 깊이 제한

n = int(input()) # 컴퓨터의 수 (노드 개수)
m = int(input()) # 연결 쌍 수 (링크 개수)
visited = [0] * (n+1) # n+1에 괄호 써줬어야했네,, 바본가

graph = [[] for _ in range(n+1)]

for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

count = 0
def dfs(s):
    global count # 함수 외부에서 사용된 변수를 사용하기 위해 global 선언해줌
    visited[s] = 1
    for i in graph[s]:
        if visited[i] == 0:
            dfs(i)
            count += 1

dfs(1)
print(count)