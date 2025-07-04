# 백준 10250 - ACM 호텔
import sys 
input = sys.stdin.readline 

t = int(input())
for _ in range(t):
    h, w, n = map(int, input().split())
    y = (n % h)   # 층
    x = n // h + 1 # 방번호
    if n % h == 0:
        x = n // h
        y = h
    print(f"{y}{x:02d}")