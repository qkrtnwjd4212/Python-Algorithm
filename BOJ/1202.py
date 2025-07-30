# 백준 1202 - 보석 도둑
import sys
import heapq
input = sys.stdin.readline

n, k = map(int, input().split())
jewel, bag = [], [] # 보석 무게, 보석 가격, 가방 무게

for _ in range(n):
    m, v = map(int, input().split())
    jewel.append((m, v))
for _ in range(k):
    bag.append(int(input()))

jewel.sort(key=lambda x: (x[0]))
bag.sort()

max_value = 0
h = []
p = 0 # 보석 무게용 포인터

for i in range(k):
    while p<n and jewel[p][0] <= bag[i]:
        heapq.heappush(h, -jewel[p][1])
        p += 1

    if h:
        max_value += (-heapq.heappop(h))

print(max_value)
