# 백준 2468 - 안전 영역
import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
max_h = max([max(row) for row in arr])
max_value = 0

def bfs(x, y, visited, amnt):
    q = deque([(x, y)])
    visited[x][y] = True

    while q:
        cx, cy = q.popleft()
        for i in range(4):
                nx, ny = cx + dx[i], cy + dy[i]
                if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                    if arr[nx][ny] > amnt:
                        visited[nx][ny] = True
                        q.append((nx, ny))

for height in range(0, max_h+1):
    visited = [[False] * n for _ in range(n)]
    cnt = 0

    for i in range(n):
        for j in range(n):
            if not visited[i][j] and arr[i][j] > height:
                bfs(i, j, visited, height)
                cnt += 1
    max_value = max(cnt, max_value)

print(max_value)