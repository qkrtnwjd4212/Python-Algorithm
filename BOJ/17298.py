# 백준 17298 - 오큰수
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
stack = []
ans = [0] * n

for i in range(n):
    while stack and arr[i] > arr[stack[-1]]:
        idx = stack.pop()
        ans[idx] = arr[i]
    stack.append(i)

for i in stack:
    ans[i] = -1

print(*ans)