# 백준 9251 - LCS
import sys 
input = sys.stdin.readline

a = input().rstrip()
b = input().rstrip()

dp = [[0] * (len(b)+1) for _ in range(len(a)+1)]

for i in range(1, len(a)+1):
    for j in range(1, len(b)+1):
        if a[i-1] == b[j-1]: # 비교하는 두 문자가 같을 때
            dp[i][j] = dp[i-1][j-1] + 1 # 이전 LCS의 길이 + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[-1][-1])

