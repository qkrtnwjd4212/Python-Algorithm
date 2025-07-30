# 백준 10844 - 쉬운 계단 수
import sys
input = sys.stdin.readline

n = int(input())

# =========== DP 안쓰고 그냥 재귀로 푼 버전 ===========
# num_list = []
#
# def f(l, s):
#     if l == n:
#         num_list.append(s)
#         return
#     last = int(s[-1])
#     if last != 9:
#         f(l+1, s + str(last+1))
#     if last != 0:
#         f(l+1, s + str(last-1))
#
# for i in range(1, 10):
#     f(1, str(i))
#
# print(num_list)
# print(len(num_list))

dp = [[0] * 10 for _ in range(n)]
dp[0] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]

for num in range(1, n):
    dp[num][0] = dp[num - 1][1]  # 끝자리가 0
    dp[num][9] = dp[num - 1][8]  # 끝자리가 9

    for k in range(1, 9):  # 끝자리가 1~8
        dp[num][k] = dp[num - 1][k - 1] + dp[num - 1][k + 1]

print(sum(dp[n - 1]) % 1000000000)