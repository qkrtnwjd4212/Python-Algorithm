# 백준 11866 - 요세푸스 문제 0
import sys
input = sys.stdin.readline
from collections import deque

N, K = map(int, input().split())
q = deque(range(1, N+1))
res = []

def josepus(n, k):
    while q:
        for i in range(k-1):
            q.rotate(-1)
        res.append(q.popleft()) # 0번 삭제
    print("<" + ", ".join(map(str, res)) + ">")

josepus(N, K)