# 백준 4948 - 베르트랑 공준
import math
import sys 
input = sys.stdin.readline 

while True:
    n = int(input())
    if n == 0:
        break

    count = 0
    arr = [True for _ in range(n*2 + 1)]
    for i in range(2, int(math.sqrt(n*2)) + 1):
        if arr[i]:
            # j = 2
            # while i*j <= n*2:
            #     arr[i*j] = False
            #     j += 1
            for j in range(i*2, 2*n + 1, i):
                arr[j] = False
    for i in range(n+1, n*2+1): 
        if arr[i]:
            count += 1
    print(count)
