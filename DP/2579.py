# 백준 2579 - 계단
# 96퍼에서 런타임 에러 ㅠㅠ
import sys 
input = sys.stdin.readline

n = int(input())
score = []
for _ in range(n):
    score.append(int(input()))

dp = [0] * n
dp[0] = score[0]
dp[1] = score[0] + score[1]

for i in range(2, n): # 점화식
    dp[i] = max(dp[i-3] + score[i-1] + score[i], dp[i-2] + score[i])
    
if n <= 2:
    print(sum(score))
else:
    print(dp[n-1])