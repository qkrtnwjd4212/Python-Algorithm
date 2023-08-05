import sys
input = sys.stdin.readline

k, n = map(int, input().rstrip().split())
lan = []
for i in range(k):
    lan.append(int(input()))

start = 1
end = max(lan)

result = 0
while start <= end:
    mid = (start + end) // 2
    total = 0 # 현재 mid값으로 만들 수 있는 랜선의 개수

    for i in lan: # 랜선 돌면서 total 값 계산
        total += (i // mid)

    if total < n: 
        end = mid - 1
    else:
        start = mid + 1

print(end)  # mid가 아니라 end가 최대 길이!! 
     

