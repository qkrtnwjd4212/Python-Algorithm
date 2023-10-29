# 백준 10026 - 적록색약
import sys
input = sys.stdin.readline

N, new, P = map(int, input().split())
rank = [list(map(int, input().split())) for _ in range(N)]

print(rank)