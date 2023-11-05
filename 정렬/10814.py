# 백준 10814 - 나이순 정렬
import sys
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    age, name = map(str, input().rstrip().split())
    age = int(age)
    arr.append([age, name])

arr.sort(key=lambda x: x[0])
for i in range(N):
    print(arr[i][0], arr[i][1])