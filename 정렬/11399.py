# 백준 11399 - ATM
import sys

input = sys.stdin.readline

n = int(input().rstrip()) # rstrip : 개행문자 제거
p = list(map(int, input().rstrip().split())) 

p.sort()

sum = p[0]
for i in range(n-1):
    p[i+1] += p[i]
    sum += p[i+1]

print(sum)