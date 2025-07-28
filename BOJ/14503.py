# 백준 14503 - 로봇청소기
import sys
input = sys.stdin.readline

n, m = map(int, input().split()) # n - 행, m - 열
cx, cy, d = map(int, input().split()) # 처음 위치, 방향 (0~3, 북-동-남-서)
cnt = 0 # 청소하는 칸의 개수
arr = [] # 0이면 빈칸, 1이면 벽 - 2면 청소 완료!!
for _ in range(n):
    arr.append(list(map(int, input().split())))

dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1] # 북-동-남-서

# 주변 4칸중에 빈칸이 없는지 확인
def check_around_clean(x, y):
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if arr[nx][ny] == 0:
                return True
    return False

while True:
    if arr[cx][cy] == 0:
        arr[cx][cy] = 2 # 현재 칸 청소
        cnt += 1

    if not check_around_clean(cx, cy): # 주변에 빈칸이 없는 경우
        nx, ny = cx - dx[d], cy - dy[d]
        if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] != 1: # 후진할 수 있다면
            cx, cy = nx, ny # 한칸 후진
            continue
        else: # 후진할 수 없다면 작동 멈춤
            break
    else: # 청소되지 않은 빈칸이 있는 경우
        for i in range(4):
            d = (d + 3) % 4  # 리스트에서 왼쪽으로 한칸씩 이동 (반시계 회전)
            nx, ny = cx + dx[d], cy + dy[d]
            if arr[nx][ny] == 0:
                cx, cy = nx, ny
                break

# for row in arr:
#     print(*row)
print(cnt)