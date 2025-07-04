# 백준 10866 - 덱
import sys
def input(): return sys.stdin.readline()
from collections import deque

N = int(input())
q = deque()

for _ in range(N):
    str = input().split()
    if len(str) > 1:
        str[1] = int(str[1])

    if str[0] == 'push_front':
        q.appendleft(str[1])
    elif str[0] == 'push_back':
        q.append(str[1])
    elif str[0] == 'pop_front':
        if q:
            print(q.popleft())
        else:
            print("-1")
    elif str[0] == 'pop_back':
        if q:
            print(q.pop())
        else:
            print("-1")
    elif str[0] == 'size':
        print(len(q))
    elif str[0] == 'empty':
        print("1" if not q else "0")
    elif str[0] == 'front':
        # if q:
        #     q.popleft()
        #     q.appendleft(str[1])
        # else:
        #     print("-1")
        print(q[0] if q else "-1")
    elif str[0] == 'back':
        # if q:
        #     q.pop()
        #     q.append(str[1])
        # else:
        #     print("-1")
        print(q[-1] if q else "-1")
    else:
        print("error")



    