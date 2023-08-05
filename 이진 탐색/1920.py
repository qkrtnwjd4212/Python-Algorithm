# 백준 1920 - 수 찾기

import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
a.sort()

m = int(input())
b = list(map(int, input().split()))

for i in range(m):
    start = 0
    end = n - 1

    ck = 0
    while start <= end:
        mid = (start + end) // 2
        if a[mid] == b[i]:
            print("1")
            ck = 1
            break
        elif a[mid] > b[i]:
            end = mid - 1
        else:
            start = mid + 1
    
    if ck == 0:
        print("0")
