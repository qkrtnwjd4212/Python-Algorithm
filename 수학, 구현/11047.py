# 백준 11047 - 동전 0
import sys
input = sys.stdin.readline

N, K = map(int, input().split()) # 동전 종류, 합
A = [int(input()) for _ in range(N)] 
count = 0

for i in range(len(A)-1, -1, -1):
    if A[i] > K:
        continue
    count += K // A[i]
    K = K % A[i]

print(count)
