# 백준 1259 - 팰린드롬수
import sys
input = sys.stdin.readline 

while True:
    n = input().rstrip()
    if n == '0':
        break
    else:
        for i in range(len(n)//2):
            if n[i] != n[-i-1]:
                print("no")
                break
        else:
            print("yes")