# 백준 2206 - 벽 부수고 이동하기
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split()) # 행, 열
arr = []
for _ in range(n):
    arr.append(list(map(int, input().strip())))

# [x][y][z], z=0: 벽 안부수고 도착, z=1: 벽 부수고 도착한 상태
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
ans = -1
dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1]

def bfs():
    global ans
    q = deque([(0, 0, 1, 0)])
    visited[0][0][0] = True

    while q:
        x, y, dist, broken = q.popleft()
        #print(dist)

        if x == n-1 and y == m-1: # 도착하면
            ans = dist
            return

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                # 다음칸이 길이면서 방문 안했을때
                if arr[nx][ny] == 0 and visited[nx][ny][broken] == 0:
                    visited[nx][ny][broken] = 1
                    q.append((nx, ny, dist+1, broken)) # 큐에 추가

                # 다음칸이 벽이면서 아직 안부쉈고 방문 안했을때
                elif arr[nx][ny] == 1 and broken == 0 and visited[nx][ny][1] == 0:
                    visited[nx][ny][1] = 1
                    q.append((nx, ny, dist+1, 1))

bfs()
print(ans)
