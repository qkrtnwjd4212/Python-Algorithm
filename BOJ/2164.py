# 백준 2164 - 카드2
import sys
def input(): return sys.stdin.readline()
from collections import deque

N = int(input())
q = deque()

for i in range(1, N+1):
    q.append(i)

while len(q) > 1:
    q.popleft()
    top = q.popleft()
    q.append(top)

result = q.popleft()
print(result)


