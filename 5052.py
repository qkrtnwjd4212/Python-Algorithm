# 백준 5052 - 전화번호 목록
import sys 
input = sys.stdin.readline 

t = int(input())
for _ in range(t):
    n = int(input()) # 전화번호 수
    nums = []
    for _ in range(n):
        nums.append(input().rstrip())
    nums.sort()

    flag = True
    for i in range(len(nums)-1):
        #if nums[i] in nums[i+1]:
        if nums[i] == nums[i+1][:len(nums[i])]:
            flag = False
            break
    if flag:
        print("YES")
    else:
        print("NO")
