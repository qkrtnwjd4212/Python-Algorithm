# 백준 1932 - 정수 삼각형
# 맨위부터 하나씩 선택한 수의 최대 합
import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

dp = [[0] * n for _ in range(n)]
dp[0][0] = arr[0][0]

for i in range(1, n):
    for j in range(i+1):
        if j == 0:
            dp[i][j] = dp[i-1][0] + arr[i][j]
        elif j == i:
            dp[i][j] = dp[i-1][j-1] + arr[i][j]
        else:
            dp[i][j] = max(dp[i-1][j-1] + arr[i][j], dp[i-1][j] + arr[i][j])

print(max(dp[-1]))