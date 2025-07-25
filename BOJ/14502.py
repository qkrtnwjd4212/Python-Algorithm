# 백준 14502 - 연구소
import sys
input = sys.stdin.readline
from collections import deque
import copy

# 0 - 빈칸, 1 - 벽, 2 - 바이러스
# 벽 3개 세워서 만들수있는 안전영역의 최대값
n, m = map(int, input().split()) # 세로, 가로
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
res = 0 # 안전영역 최대값

# 안전영역 크기 구하기
def bfs(new_arr, virus):
    q = deque()
    for v in virus:
        q.append(v)

    while q:
        cx, cy = q.pop()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < n and 0 <= ny < m and new_arr[nx][ny] == 0:
                q.append((nx, ny))
                new_arr[nx][ny] = 2

    count = 0
    for i in range(n):
        for j in range(m):
            if new_arr[i][j] == 0:
                count += 1
    return count

# 벽 세울 수 있는 공간, 바이러스 좌표 구하기
wall_space = []
virus = []
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            wall_space.append((i, j))
        elif arr[i][j] == 2:
            virus.append((i, j))

# 가능한 모든 벽 조합 탐색
for i in range(len(wall_space)):
    for j in range(i+1, len(wall_space)):
        for k in range(j+1, len(wall_space)):
            x1, y1 = wall_space[i] # wall 1
            x2, y2 = wall_space[j] # wall 2
            x3, y3 = wall_space[k] # wall 3

            new_arr = copy.deepcopy(arr)
            new_arr[x1][y1], new_arr[x2][y2], new_arr[x3][y3] = 1, 1, 1

            tmp = bfs(new_arr, virus)
            #print(tmp)
            res = max(res, tmp)

print(res)


