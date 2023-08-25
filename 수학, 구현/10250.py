# 백준 10250 - ACM 호텔
import sys 
input = sys.stdin.readline 

t = int(input())
for _ in range(t):
    h, w, n = map(int, input().split())
    y, x = 0, 1
    y += (n % h)   # 층
    x += n // h  # 방번호
    if h == 1:
        print(f"1{n:02d}")
    else:
        print(f"{y}{x:02d}")