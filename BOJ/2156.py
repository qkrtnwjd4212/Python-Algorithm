# 백준 2156 - 포도주 시식
# 연속된 3잔은 못마실 때, 마실 수 있는 포도주 양의 최대
import sys
input = sys.stdin.readline

n = int(input()) # 잔 개수
a = [0] # 포도주 amount
for _ in range(n):
    a.append(int(input()))
if n == 1:
    print(a[1])
    sys.exit()
elif n == 2:
    print(a[1] + a[2])
    sys.exit()

dp = [0] * (n+1)
dp[1], dp[2] = a[1], a[1] + a[2]

for i in range(3, n+1):
    dp[i] = max(
        dp[i-1],
        dp[i-2] + a[i],
        dp[i-3] + a[i-1] + a[i]
    )

#print(dp)
print(dp[n])