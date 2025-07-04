# 백준 10950 - A+B-3
import sys 
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    print(a+b)