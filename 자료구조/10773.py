# 백준 10773 - 제로
import sys 
input = sys.stdin.readline 

k = int(input())
stack = []
for i in range(k):
    n = int(input())
    if n == 0:
        stack.pop()
    else:
        stack.append(n)

print(sum(stack))