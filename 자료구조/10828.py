# 백준 10828 - 스택
import sys
input = sys.stdin.readline

N = int(input().strip()) # 이거 왜 공백제거해줘야하는데!!!!미쳤나 하
stack = []
for i in range(N):
    now = list(input().rstrip().split())

    if now[0] == 'push':
        stack.append(int(now[1]))
        
    elif now[0] == 'pop':
        if len(stack) == 0: print(-1)
        else: print(stack.pop())

    elif now[0] == 'size':
        print(len(stack))

    elif now[0] == 'empty':
        if len(stack) == 0: print(1)
        else: print(0)

    elif now[0] == 'top':
        if len(stack) == 0: print(-1)
        else: print(stack[-1])
