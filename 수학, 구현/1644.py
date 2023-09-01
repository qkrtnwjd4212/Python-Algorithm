# 백준 1644 - 소수의 연속합
import math
import sys
input = sys.stdin.readline 

n = int(input())
prime = []

# n 이하의 소수 구하기
arr = [True for _ in range(n+1)]
for i in range(2, int(math.sqrt(n)) + 1):
    if arr[i] == True:
        j = 2
        while i*j <= n:
            arr[i*j] = False
            j += 1

for i in range(2, n+1): 
    if arr[i]:
        prime.append(i)

start, end, count = 0, 0, 0
while end <= len(prime):
    tmp = sum(prime[start:end])
    if tmp == n:
        count += 1
        start += 1
    elif tmp < n:
        end += 1
    else:
        start += 1

print(count)