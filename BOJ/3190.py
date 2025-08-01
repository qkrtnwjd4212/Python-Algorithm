# 백준 3190 - 뱀
import sys
input = sys.stdin.readline
from collections import deque

# ====================== 입력받기 ======================
n = int(input())
k = int(input())
arr = [[0] * n for _ in range(n)] # 0 - 빈칸, 2 - 사과

for _ in range(k):
    x, y = map(int, input().split())
    arr[x-1][y-1] = 2

l = int(input())
dir_change = {} # 방향 전환 정보
for i in range(l): # a초가 끝난 뒤에 b 방향으로 회전
    a, b = input().split()
    dir_change[int(a)] = b

# ====================== 메인 로직 ======================
time = 0
dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1] # 상좌하우
dir = 3 # 초기 방향 오른쪽

snake = deque([(0, 0)]) # 머리가 왼쪽, 꼬리가 오른쪽
arr[0][0] = 1

while True:
    time += 1 # 먼저 시간 증가

    # 다음 머리 위치 계산
    x, y = snake[0] # 현재 머리 위치
    nx, ny = x + dx[dir], y + dy[dir]

    # 벽/뱀에 부딪힌 경우 게임 종료
    if not (0 <= nx < n and 0 <= ny < n) or arr[nx][ny] == 1:
        break

    snake.appendleft((nx, ny)) # 머리 한칸 이동
    if arr[nx][ny] == 2: #사과가 있다면
        arr[nx][ny] = 1
    else:
        arr[nx][ny] = 1
        tx, ty = snake.pop() # 꼬리 (제일 오른쪽) 한칸 제거
        arr[tx][ty] = 0 # 꼬리 칸 빈칸으로

    if time in dir_change:
        if dir_change[time] == 'L':  # 왼쪽, idx + 1
            dir = (dir + 1) % 4
        else:  # 오른쪽, idx - 1
            dir = (dir - 1) % 4

print(time)


