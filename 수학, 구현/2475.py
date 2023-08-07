# 백준 2475 - 검증수
import sys 
input = sys.stdin.readline

num = list(map(int, input().rstrip().split()))
sum = 0
for i in num:
    sum += i*i

print(sum % 10)