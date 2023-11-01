# 백준 2529 - 부등호
import sys
input = sys.stdin.readline

k = int(input())
sign = list(map(str, input().rstrip().split()))
nums = []
modumanjok = []

def backtracking(level): # 좋은 수열 백트래킹 참고
    # 숫자랑 부등호랑 비교해가면서 성립 안하면 백트래킹 빠져나오는 부분
    for i in range(len(sign)): 
        if len(nums) <= i+1: # nums에 부등호 비교할 숫자 모자라면 빠져나가기
            break
        else:
            if sign[i] == '<':
                result = nums[i] < nums[i+1]
            else:
                result = nums[i] > nums[i+1]
            if result == False:
                return 0

    if level == len(sign)+1:
        modumanjok.append(''.join(map(str, nums)))
        return 1

    for i in range(10):
        if i not in nums: # 중복 방지
            nums.append(i)
            backtracking(level+1)
            nums.pop()

backtracking(0)
#print(modumanjok)
modumanjok.sort()
print(modumanjok[-1])
print(modumanjok[0])
