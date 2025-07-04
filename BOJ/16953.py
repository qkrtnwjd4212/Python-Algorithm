# 백준 16953 - A->B
import sys 
input = sys.stdin.readline

a, b = map(int, input().split())
count = 0

while b != a:
    if b < a:
        count = -2
        break
    elif b % 2 == 0:
        b //= 2
        count += 1
    elif b % 10 == 1:
        b //= 10
        count += 1
    else:
        count = -2
        break

print(count + 1)