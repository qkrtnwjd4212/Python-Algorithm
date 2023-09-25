# 백준 11651 - 좌표 정렬하기 2
import sys
input = sys.stdin.readline

N = int(input())
coor = [list(map(int, input().split())) for _ in range(N)]

coor.sort(key= lambda x: (x[1], x[0]))
for i in range(N):
    print(coor[i][0], coor[i][1])