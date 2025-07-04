# 백준 27866 - 문자와 문자열
import sys 
input = sys.stdin.readline 

word = input().rstrip()
n = int(input())
print(word[n-1])