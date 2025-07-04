# 백준 11650 - 좌표 정렬하기
import sys
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    a, b = map(int, input().split())
    arr.append([a, b])

arr.sort(key=lambda x: (x[0], x[1]))
for i in range(N):
    print(arr[i][0], arr[i][1])