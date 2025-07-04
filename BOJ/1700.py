# 백준 1700 - 멀티탭 스케줄링
import sys 
input = sys.stdin.readline

N, K = map(int, input().split()) # 멀티탭 구멍 수, 사용횟수
seq = list(map(int, input().split()))
plug = []
count = 0

for i in range(K):
    now = seq[i] # 현재 전자제품

    if now in plug: # 사용해야하는게 멀티탭에 있으면
        continue
    if len(plug) < N: # 멀티탭이 아직 비었으면
        plug.append(now) # 걍 넣기
        continue

    else: # 멀티탭이 찼으면 -> 하나 빼고 현재 전자제품 넣기
        # 뒤에 써야할 횟수가 적은거 -> 많이 나와도 뒤에 몰려있으면 먼저 빼는게 좋음
        # 가장 나중에 사용되는거 기준으로!! (횟수 말고 순서)
        tmp, maximum = 0, 0
        for plugged in plug:
            if plugged not in seq[i:]: # 멀티탭에 꽂힌게 나중에 안나오면 빼기
                tmp = plugged
                break
            elif seq[i:].index(plugged) > maximum:
                maximum = seq[i:].index(plugged)
                tmp = plugged
        plug[plug.index(tmp)] = now
        count += 1

print(count)