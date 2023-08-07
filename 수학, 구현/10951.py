# 백준 10950 - A+B-3
import sys 
input = sys.stdin.readline


while(1):
    try:    
        a, b = map(int, input().split())
        print(a+b)
    except:
        break