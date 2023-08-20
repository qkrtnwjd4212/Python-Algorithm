# 백준 10871 - X보다 작은 수
import sys 
input = sys.stdin.readline 

N, X = map(int, input().split())
arr = list(map(int, input().rstrip().split()))

for i in arr:
    if i < X:
        print(i, end=' ') 