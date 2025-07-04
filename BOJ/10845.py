# 백준 10845 - 큐
import sys
def input(): return sys.stdin.readline()
from collections import deque

q = deque()
N = int(input())

for _ in range(N):
    str = input().split()
    if len(str) > 1:
        str[1] = int(str[1])

    if str[0] == 'push':
        q.append(str[1])
    elif str[0] == 'pop':
        if q:
            num = q.popleft()
            print(num)
        else:
            print(-1)
    elif str[0] == 'size':
        print(len(q))
    elif str[0] == 'empty':
        if q: print(0)
        else: print(1)
    elif str[0] == 'front':
        if q:
            num = q.popleft()
            print(num)
            q.appendleft(num)
        else:
            print(-1)
    elif str[0] == 'back':
        if q:
            num = q.pop()
            print(num)
            q.append(num)
        else:
            print(-1)

    

