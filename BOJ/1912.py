# 백준 1912 - 연속합
# 연속된 몇개의 수의 최대 합
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
max_sum = -1000
cur_sum = 0

for i in range(0, n):
    cur_sum = max(cur_sum + arr[i], arr[i])
    max_sum = max(max_sum, cur_sum)

print(max_sum)
