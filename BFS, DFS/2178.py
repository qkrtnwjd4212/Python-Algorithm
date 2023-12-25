# 백준 2178 - 미로 탐색
import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
miro = [list(map(int, input().strip())) for _ in range(N)]

dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
min_dis = float('inf') # 무한대

def bfs(x, y):
    global min_dis
    q = deque([(x, y, 1)])

    while q:
        cur_x, cur_y, cnt = q.popleft()
        if cur_x == N-1 and cur_y == M-1:
            return cnt

        for i in range(4):
            nx, ny = cur_x + dx[i], cur_y + dy[i]
            
            if 0 <= nx < N and 0 <= ny < M and miro[nx][ny] == 1:
                miro[nx][ny] = 0 # 방문 표시
                q.append((nx, ny, cnt+1))

print(bfs(0,0))