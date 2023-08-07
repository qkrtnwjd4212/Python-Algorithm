# 백준 2739 - 구구단
import sys 
input = sys.stdin.readline

n = int(input())
for i in range(1, 10):
    print(f'{n} * {i} = {n*i}')