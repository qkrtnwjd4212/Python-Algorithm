# 백준 1697 - 숨바꼭질
# 걸으면 -> 1씩 이동, 순간이동 -> 2배
# 수빈이가 동생을 찾을 수 있는 가장 빠른 시간
import sys 
input = sys.stdin.readline
from collections import deque

N, K = map(int, input().split()) # 수빈, 동생
cnt = [-1] * (100001)
cnt[N] = 0

q = deque([N])
while q:
    cur = q.popleft()
    for next in (cur+1, cur-1, cur*2):
        if 0 <= next <= 100000 and cnt[next] == -1:
            cnt[next] = cnt[cur] + 1
            q.append(next)

#print(cnt)
print(cnt[K])



