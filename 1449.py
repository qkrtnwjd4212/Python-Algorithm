# 백준 1449 - 수리공 항승
import math 
import sys 
input = sys.stdin.readline

N, L = map(int, input().split()) # 개수, 길이
loc = list(map(int, input().split())) # 위치
loc.sort()

# count = 0
# i = 0
# while i < len(loc)-1:
#         a, b = loc[i], loc[i+1]
#         if b >= a + L: # 테이프의 길이 이상 차이나면
#             count += math.ceil((a - loc[0] + 1) / L) # 나눈 후 올림
#             loc = loc[i+1:] # b 앞의 값들 삭제
#             i = 0
#             continue
#         i += 1
# count += math.ceil((loc[-1] - loc[0] + 1) / L)

start = loc[0]
count = 1 # 시작지점 테이프 한개 붙여주기
for i in loc[1:]: # loc를 돌면서
    if i in range(start, start+L): # i가 start에서 테이프 길이 이내면
        continue # 그냥 넘어가기
    else: # 테이프 길이를 넘었으면
        start = i # 현재 구간을 start로 업데이트,
        count += 1 # 테이프 개수 증가

print(count)
