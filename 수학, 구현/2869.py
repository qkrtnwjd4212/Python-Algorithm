# 백준 2869 - 달팽이는 올라가고 싶다
import sys 
input = sys.stdin.readline
import math

a, b, v = map(int, input().split())
day = math.ceil((v-a) / (a-b))
print(day+1)
