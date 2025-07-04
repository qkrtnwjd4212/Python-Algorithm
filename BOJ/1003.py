# 백준 1003 - 피보나치 함수
import sys 
input = sys.stdin.readline

# 시간 초과..!!
# t = int(input())
# n = [int(input()) for _ in range(t)]
# dp = [-1] * (max(n) + 1)
# dp[0], dp[1] = 0, 1

# c0, c1 = 0, 0
# def fib(n):
#     global c0, c1
#     if n == 0:
#         c0 += 1
#         return 0
#     elif n == 1:
#         c1 += 1
#         return 1
#     else:
#         if dp[n] != -1:
#             return dp[n]
#         else:
#             return (fib(n-1) + fib(n-2))

# for i in range(t):
#     fib(n[i])
#     print(c0, c1)
#     c0, c1 = 0, 0

t = int(input())

# 0, 1이 출력되는 횟수
zero, one = [1,0,1], [0,1,1]

def fib(n):
    l = len(zero)
    if n >= l:
        for i in range(l, n+1):
            zero.append(zero[i-1] + zero[i-2])
            one.append(one[i-1] + one[i-2])
    print(zero[n], one[n])

for _ in range(t):
    fib(int(input()))
