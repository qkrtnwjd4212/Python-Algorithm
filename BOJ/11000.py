# 백준 11000 - 강의실 배정
import sys
input = sys.stdin.readline
from heapq import heappush, heappop, heapify

n = int(input())
time = []

for i in range(n):
    s, t = map(int, input().split())
    time.append([s, t])
time.sort()
room = [time[0][1]] # 첫번째 강의는 그냥 넣기
for i in range(1, n):
    if room[0] <= time[i][0]:
        heappop(room)
    heappush(room, time[i][1])

print(len(room))