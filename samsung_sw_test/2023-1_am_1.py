from collections import deque

n, m, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)] # 공격력

arr_info = [] # 포탑 정보 저장 (공격력, 공격 시점, 행, 열)
attack_time = [[0] * m for _ in range(n)] # 첫 공격 시점은 0으로 초기화
attacker = (-1, -1) # 공격자 (가장 약한 포탑)
target = (-1, -1) # 공격 대상 (가장 강한 포탑)

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def is_in_range(x, y, m, n):
    return 0 <= x < n and 0 <= y < m

# 포탑 정보 만들기 ====================================
def init():
    for i in range(n):
        for j in range(m):
            if arr[i][j] > 0:
                arr_info.append((arr[i][j], attack_time[i][j], i, j))

# 공격자(가장 약한 포탑)과 공격 대상(가장 강한 포탑) 찾기 ==================
def find_attacker_and_target():
    global attacker, target
    # 공격력: 작은거, 공격시점: 큰거, 행+열: 큰거, 열: 큰거
    weakest = min(arr_info, key=lambda x: (x[0], -x[1], -(x[2]+x[3]), -x[3]))
    #print(weakest)
    attacker = (weakest[2], weakest[3])
    ax, ay = attacker

    # 공격자 공격력 올리고 공격시점 업데이트
    arr[ax][ay] += (m + n)
    attack_time[ax][ay] += 1

    strong = max(arr_info, key=lambda x: (x[0], -x[1], -(x[2]+x[3]), -x[3]))
    #print(strong)
    target = (strong[2], strong[3])


def range_check(x, y, m, n):
    if x < 0:
        return (n-1, y)
    elif x == n:
        return (0, y)
    elif y < 0:
        return (x, m-1)
    elif y == m:
        return (x, 0)

# 레이저 공격 ====================================
def laser(start, end):
    q = deque([attacker])
    visited = {start} # 방문한 노드 저장
    parent = {start: None} # 경로 역추적용 {자식: 부모}

    path_found = False
    while q:
        x, y = q.popleft()

        if (x, y) == end: # 타겟에 도착
            path_found = True
            break # bfs 종료

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not is_in_range(nx, ny, m, n): # 인덱스 범위를 벗어나면
                nx, ny = range_check(nx, ny, m, n) # 반대편으로 값 보정

            if arr[nx][ny] != 0 and (nx, ny) not in visited: # 포탑 공격력이 0이 아닐때만
                visited.add((nx, ny))
                parent[(nx, ny)] = (x, y) # 이전 노드(부모) 기록
                q.append((nx, ny))

    if not path_found:
        return None # 최단 경로 없음

    path = []
    current = end
    while current is not None:
        path.append(current)
        current = parent[current]

    ax, ay = attacker
    for x, y in path: # 최단 경로를 돌면서
        if (x, y) == target: # 공격 대상이면 공격력만큼 피해
            arr[x][y] -= arr[ax][ay]
        else: # 공격 대상이 아니면 공격력의 절반만큼 피해
            arr[x][y] -= (arr[ax][ay] / 2)


# 포탄 공격 ====================================
def bomb(start, end):
    print()



# ================== 시뮬레이션 ==================
init()
find_attacker_and_target()
print(attacker)
print(target)
