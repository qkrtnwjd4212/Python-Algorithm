# 백준 2798 - 블랙잭
# 카드 N장 중 합이 M을 넘지 않으면서 최대한 크게
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
card = list(map(int, input().split()))
max_sum = 0

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
                tmp_sum = card[i] + card[j] + card[k]
                if max_sum < tmp_sum and tmp_sum <= M:
                     max_sum = tmp_sum

print(max_sum)




