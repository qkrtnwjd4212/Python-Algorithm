# 백준 2609 - 최대공약수와 최소공배수
import sys
input = sys.stdin.readline

a, b = map(int, input().split())

def gcd(x, y):
    while(y):
        x, y = y, x%y
    return x

def lcm(x, y):
    res = (x*y) // gcd(x,y)
    return res

print(gcd(a,b))
print(lcm(a,b))