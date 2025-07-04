# 백준 11720 - 숫자의 합
import sys 
input = sys.stdin.readline 

nums = []
for _ in range(9):
    n = int(input())
    nums.append(n)

print(max(nums))
print(nums.index(max(nums)) + 1)  # index() : 해당하는 값의 인덱스를 출력
