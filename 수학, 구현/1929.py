# 백준 1929 - 소수 구하기
import math
import sys 
input = sys.stdin.readline 

m, n = map(int, input().split())
arr = [True for _ in range(n+1)]

for i in range(2, int(math.sqrt(n)) + 1):
    if arr[i] == True:
        j = 2
        while i*j <= n:
            arr[i*j] = False
            j += 1

# m이 1일수도 있어서 예외처리 
for i in range(max(2,m), n+1): 
    if arr[i]:
        print(i)
