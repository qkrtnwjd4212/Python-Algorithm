# 백준 1107 - 리모컨
import sys
input = sys.stdin.readline

n = int(input()) # 이동하려고 하는 채널
m = int(input()) # 고장난 버튼의 개수
wrong_btn = list(map(int, input().split())) # 고장난 버튼
cnt = 0
diff_min = abs(n-100) # 증감 버튼만 눌러서 이동하는 횟수

# N (0 ≤ N ≤ 500,000) 이므로 그 2배까지 탐색
for i in range(1000000): # 0부터 1,000,000까지 탐색
    # i에 고장난 버튼이 없는지 확인
    chk = True
    for digit in str(i):
        if int(digit) in wrong_btn:
            chk = False
            break

    # 없으면 -> 최솟값 갱신
    if chk:
        tmp = len(str(i)) + abs(n-i)
        diff_min = min(tmp, diff_min)

print(diff_min)

