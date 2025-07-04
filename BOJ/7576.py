# 백준 7576 - 토마토
import sys 
input = sys.stdin.readline
from collections import deque

queue = deque()
m, n = map(int, input().split()) # 가로, 세로
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))
    # 입력받으면서 썩은 토마토가 있는 위치만 큐에 넣어주기
    for j in range(m):
        if graph[i][j] == 1:
            queue.append([i, j])

# 상하좌우 방향
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append([nx, ny])

result = 0      
bfs()
for i in graph:
    if 0 in i:
        print("-1")
        exit() # 안익은게 있는 경우, 반복문 밑에서 result 출력하지 않도록 break가 아니라 exit으로 프로그램 종료
    result = max(result, max(i))

print(result - 1) # 날짜를 2일부터 시작했으므로 -1
