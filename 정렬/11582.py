# 백준 11582 - 치킨 TOP N
import sys
input = sys.stdin.readline

N = int(input()) # 치킨집 개수
chicken = list(map(int, input().split()))
k = int(input()) # 정렬 진행중인 회원 수

# k명이 정렬 진행한 뒤의 상태 -> N//k 씩 A를 나눠서 정렬함
i = 0
for _ in range(k):
    arr = chicken[i:i+(N//k)]
    arr.sort()
    for j in arr:
        print(j, end=' ')
    i += (N//k)
