import sys
input = sys.stdin.readline

n, c = map(int, input().split())
house = [int(input().rstrip()) for i in range(n)]
house.sort()

start, end = 1, house[n-1] - house[0]

while start <= end:
    mid = (start + end) // 2

    # 첫번째 집에는 무조건 설치
    current = house[0] 
    count = 1

    for i in range(1, n):
        if house[i] >= current + mid: # 다음 집이 현재 집에서 mid 이상 떨어져 있을 때만
            count += 1 # 공유기 설치,
            current = house[i] # 현재값 업데이트
        
    if count >= c:
            start = mid + 1
    else:
            end = mid - 1

print(end)