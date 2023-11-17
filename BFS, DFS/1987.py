# 백준 1987 - 알파벳
import sys 
input = sys.stdin.readline
from collections import deque

R, C = map(int, input().split()) # 세로, 가로
arr = [list(input().rstrip()) for _ in range(R)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
count = 1

def bfs(x, y):
    global count
    #q = deque([(x, y, arr[0][0])])
    q = set([(x, y, arr[0][0])]) # 중복제거 set 사용

    while(q):
        cur = q.pop()
        count = max(count, len(cur[2]))
        for i in range(4):
            nx, ny = cur[0] + dx[i], cur[1] + dy[i]
            if 0 <= nx < R and 0 <= ny < C and arr[nx][ny] not in cur[2]:
                q.add((nx, ny, cur[2] + arr[nx][ny]))

bfs(0,0)
print(count)


