# 백준 7568 - 덩치
import sys
input = sys.stdin.readline 

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    now = 1 # 현재 비교하는 사람의 등수
    for j in range(N):
        if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
            now += 1
    print(now, end=' ')