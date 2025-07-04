# 백준 5052 - 전화번호 목록
import sys 
input = sys.stdin.readline 

#t = int(input())
for _ in range(int(input())):
    n = int(input()) # 전화번호 수
    #nums = [input().rstrip() for _ in range(n)] 
    nums = []
    for _ in range(n):
        nums.append(input().rstrip())
    nums.sort()

    flag = True
    for i in range(len(nums)-1):
        #if nums[i] in nums[i+1]:
        if nums[i] == nums[i+1][:len(nums[i])]:
            #print("No")
            flag = False
            break
    # else:
    #     print("YES")
    if flag:
        print("YES")
    else:
        print("NO")
