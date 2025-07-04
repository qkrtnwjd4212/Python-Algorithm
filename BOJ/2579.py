# 백준 2579 - 계단
import sys 
input = sys.stdin.readline

n = int(input())
score = []
dp = [0] * n
for _ in range(n):
    score.append(int(input()))

if n<=2:
    print(sum(score))
else:
    dp[0] = score[0]
    dp[1] = score[0] + score[1]
    for i in range(2, n): # 점화식
        dp[i] = max(dp[i-3] + score[i-1] + score[i], dp[i-2] + score[i])
    print(dp[n-1])   
