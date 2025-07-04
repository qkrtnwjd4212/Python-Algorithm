# 백준 1715 - 카드 정렬하기
import sys
from heapq import heappush, heappop, heapify
input = sys.stdin.readline

n = int(input())
if n == 1:
    print(0)
    exit()

arr = [int(input()) for _ in range(n)]
heapify(arr)
ans = 0

while len(arr) >= 2:
    tmp = heappop(arr) + heappop(arr)
    ans += tmp
    heappush(arr, tmp)

print(ans)


