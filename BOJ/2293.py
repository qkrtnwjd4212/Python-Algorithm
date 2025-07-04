# 백준 2293 - 동전 1
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
v = []
dp = [0] * (k+1)

for _ in range(n):
    value = int(input())
    v.append(value)
    dp[value] = 1
v.sort()

for i in range(k):
    for j in range(n):
        if i + v[j] <= k:
            dp[i+v[j]] += 1

print(dp)
print(dp[k])

