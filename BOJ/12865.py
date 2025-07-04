# 백준 12865 - 평범한 배낭
import sys 
input = sys.stdin.readline

n, k = map(int, input().split())
w = [0] # 0 넣어주기...
v = [0]

for _ in range(n):
    a, b = map(int, input().split())
    w.append(a)
    v.append(b)

dp = [[0] * (k+1) for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, k+1):
        if j < w[i]:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(v[i] + dp[i-1][j - w[i]], dp[i-1][j])

print(dp[n][k])