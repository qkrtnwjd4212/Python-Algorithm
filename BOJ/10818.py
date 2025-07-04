# 백준 10818 - 최소, 최대
import sys 
input = sys.stdin.readline 

n = int(input())
nums = list(map(int, input().split()))

print(min(nums), max(nums))