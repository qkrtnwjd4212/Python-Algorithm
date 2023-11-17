# 백준 7562 - 나이트의 이동
import sys
input = sys.stdin.readline
from collections import deque

dx = [-2, -2, 2, 2, -1, -1, 1, 1]
dy = [-1, 1, -1, 1, -2, 2, -2, 2]

def bfs(x, y):
    q = deque([(x, y)])
    while q:
        now = q.popleft()
        for i in range(8):
            nx, ny = now[0] + dx[i], now[1] + dy[i]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
                visited[nx][ny] = visited[now[0]][now[1]] + 1
                q.append([nx, ny])
    return True

T = int(input())
for _ in range(T):
    N = int(input()) # 한 변의 길이
    cur_x, cur_y = map(int, input().split())
    end_x, end_y = map(int, input().split())

    visited = [[0] * N for _ in range(N)]
    #for i in range(N):
    #    for j in range(N):
    #        bfs(i,j)
    # 입력:
    # 1
    # 4
    # 1 1
    # 2 2
    # 출력:
    # 4
    # 답:
    # 2
    bfs(cur_x, cur_y)

    if cur_x == end_x and cur_y == end_y:
        print(0)
    else:
        print(visited[end_x][end_y])