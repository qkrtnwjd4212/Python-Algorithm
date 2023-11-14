# 백준 2589 - 보물섬
# L 육지, W 바다
# 상하좌우로 이웃한 육지로만 이동 가능
# 보물 : 가장 멀리 떨어진 육지 두 곳
import sys
input = sys.stdin.readline
from collections import deque

h, w = map(int, input().split())
map = [list(map(str, input().rstrip())) for _ in range(h)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def bfs(x, y):
    bomul = [[0] * w for _ in range(h)] # 각 위치에서 가장 멀리 떨어진 육지
    bomul[x][y] = 1
    q = deque([(x,y)])
    tmp = 0
    while q:
        cur = q.popleft()
        for i in range(4):
            nx, ny = cur[0] + dx[i], cur[1] + dy[i]
            if 0 <= nx < h and 0 <= ny < w and map[nx][ny] == 'L' and bomul[nx][ny] == 0: # 방문하지 않은 곳만 지나야 최단거리 출력됨
                bomul[nx][ny] = bomul[cur[0]][cur[1]] + 1
                q.append((nx, ny))
                tmp = max(tmp, bomul[nx][ny])
    return tmp-1 # 두 곳 사이의 거리니까 -1

result = 0
for i in range(h):
    for j in range(w):
        if map[i][j] == 'L':
            result = max(result, bfs(i, j))

print(result)

# 파이썬으로 하면 시간초과, pypy로 하면 통과