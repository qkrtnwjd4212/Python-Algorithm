# 백준 2675 - 문자열 반복
import sys 
input = sys.stdin.readline 

t = int(input())
for _ in range(t):
    n, word = map(str, input().split())
    n = int(n)

    res = ""
    for i in word:
        res += (i*n)
    print(res)

