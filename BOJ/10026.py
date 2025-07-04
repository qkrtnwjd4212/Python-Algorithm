# 백준 10026 - 적록색약
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

N = int(input())
graph = [list(map(str, input().rstrip())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]  # 방문 여부
count_1, count_2 = 0, 0 # 색약x, 색약o 구역 개수

def dfs(x, y, color):
    if x < 0 or x >= N or y < 0 or y >= N or visited[x][y] or graph[x][y] != color:
        return False
    visited[x][y] = True
    dfs(x - 1, y, color)
    dfs(x, y - 1, color)
    dfs(x + 1, y, color)
    dfs(x, y + 1, color)
    return True

for i in range(N):
    for j in range(N):
        if dfs(i, j, graph[i][j]) == True:
            count_1 += 1

for i in range(N): # 그래프 돌면서 visited 리스트 초기화 + R값 G로 바꾸기
    for j in range(N):
        visited[i][j] = False
        if graph[i][j] == 'R':
            graph[i][j] = 'G'

for i in range(N):
    for j in range(N):
        if dfs(i, j, graph[i][j]) == True:
            count_2 += 1

print(count_1, count_2)