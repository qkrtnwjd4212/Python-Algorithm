# 백준 1652 - 누울 자리를 찾아라
import sys
input = sys.stdin.readline

N = int(input())
arr = [list(input().rstrip()) for _ in range(N)]

def garo_count(n):
    tmp, garo = 0, 0
    for i in range(N):
        tmp = 0 # 줄 바뀌면 초기화
        for j in range(N):
            if arr[i][j] == '.':
                tmp += 1
            else:
                tmp = 0
            if tmp == 2: # 검사한 뒤 카운트
                garo += 1
        #print(f'{i}번째 가로 : {garo}')
    return garo

def sero_count(n):
    tmp, sero = 0, 0
    for j in range(N):
        tmp = 0
        for i in range(N):
            if arr[i][j] == '.':
                tmp += 1
            else:
                tmp = 0
            if tmp == 2:
                sero += 1
        #print(f'{j}번째 세로 : {sero}')
    return sero

print(garo_count(N), sero_count(N))
