# 백준 11720 - 숫자의 합
import sys 
input = sys.stdin.readline 

n = int(input())
nums = [int(num) for num in input().rstrip()]
print(sum(nums))