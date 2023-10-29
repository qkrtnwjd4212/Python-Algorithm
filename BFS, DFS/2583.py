# 백준 2583 - 영역 구하기
import sys
input = sys.stdin.readline
from collections import deque

M, N, K = map(int, input().split())
rec = [list(map(int, input().split())) for _ in range(K)] # 직사각형 좌표
arr = [[0] * N for _ in range(M)] # MxN 
area = [] # 분리된 영역 넓이

# 직사각형 내부를 1로 채우기
for i in range(K):
    b, a, d, c = rec[i][0], M - rec[i][1] - 1, rec[i][2], M - rec[i][3] - 1
    for row in range(a, c, -1):
        for col in range(b, d):
            arr[row][col] = 1
    #print(f'[{a}, {b}, {c}, {d}]')

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    q = deque([(x, y)])

    # 예제의 1번 영역은 아래 if문에 안걸림 -> tmp 기본값을 1로 설정하고 행렬값 1로 바꿔서 중복 처리 안되게 함
    tmp = 1
    arr[x][y] = 1
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < M and 0 <= ny < N and arr[nx][ny] == 0:
                tmp += 1
                q.append((nx, ny))
                arr[nx][ny] = 1
    area.append(tmp)
    return True

count = 0
for i in range(M):
    for j in range(N):
        if arr[i][j] == 0 and bfs(i,j):
                count += 1
            
print(count)
for i in sorted(area):
    print(i, end=' ')
