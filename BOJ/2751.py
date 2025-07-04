# 백준 2751 - 수 정렬하기 2
import sys
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))

arr.sort()
for i in arr:
    print(i)