# 백준 1085 - 직사각형에서 탈출
import sys 
input = sys.stdin.readline

x, y, w, h = map(int, input().split())

dist = min(y, h-y, x, w-x)
print(dist)
