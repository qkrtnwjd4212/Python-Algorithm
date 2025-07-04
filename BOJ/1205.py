# 백준 1205 - 등수 구하기
# 랭킹 리스트가 꽉 차있을 때, 새 점수가 이전 점수보다 더 좋을 때만 점수가 바뀐다.
# 랭킹 리스트에 올라 갈 수 있는 점수의 개수 
import sys
input = sys.stdin.readline

N, new, P = map(int, input().split())
if N == 0:
    print(1)
    exit()
list = list(map(int, input().split()))
rank = 1
for i in range(N):
    if list[i] > new:
        rank += 1

if rank > P or (P == N and list[P-1] == new):
    print(-1)
else:
    print(rank)


