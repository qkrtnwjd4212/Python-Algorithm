# 백준 11050 - 이항 계수 1
import sys
input = sys.stdin.readline
import math

N, K = map(int, input().split())
print(math.factorial(N) // (math.factorial(N-K) * math.factorial(K)))

# 파이썬 팩토리얼 함수 이용!!
# nCk = n! // (n-k)!k!