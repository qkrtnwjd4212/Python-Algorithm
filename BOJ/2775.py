# 백준 2775 - 부녀회장이 될테야
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    k, n = int(input()), int(input()) # k층 n호
    dp = [[0] * (n+1) for _ in range(k+1)]

    for i in range(n+1):
        dp[0][i] = i # 0층 채우기
    for i in range(1, k+1):
        dp[k][1] = 1 # 각 층의 1호는 1로
    #print(dp)
    for i in range(1, k+1):
        for j in range(1, n+1):
            dp[i][j] = dp[i][j-1] + dp[i-1][j]
    #print(dp)
    print(dp[k][n])

