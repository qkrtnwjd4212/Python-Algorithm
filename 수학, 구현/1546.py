# 백준 1546 - 평균
import sys
input = sys.stdin.readline

N = int(input())
score = list(map(int, input().split()))
max_num = max(score)

new = (sum(score) / max_num * 100) / N
print(new)