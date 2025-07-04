# 백준 1946 - 신입 사원
import sys
input = sys.stdin.readline

T = int(input())
    
# for _ in range(T):
#     N = int(input())
#     score = []
#     for _ in range(N):
#         a, b = map(int, input().split()) # 서류 순위, 면접 순위
#         score.append([a,b])
#     count = N  
#     for i in range(N):
#         ck = 0
#         for j in range(N):
#             if i == j:
#                 continue
#             # i번째가 j번째보다 서류, 면접 둘다 순위 낮다면(크다면)
#             if score[i][0] > score[j][0] and score[i][1] > score[j][1]: 
#                 ck = 1
#         if ck:
#             count -= 1
#             ck = 0
#     print(count)

for _ in range(T):
    N = int(input())
    score = []
    for _ in range(N):
        a, b = map(int, input().split()) # 서류 순위, 면접 순위
        score.append([a,b])
    
    score.sort()
    count = 1
    rank = score[0][1] # 서류 1등의 면접 순위

    for i in range(1, N):
        # 면접 순위를 계속 갱신해가면서 최소인거만 뽑음 (서류 순위는 갈수록 떨어지니까)
        if score[i][1] < rank:
            count += 1
            rank = score[i][1]
    
    print(count) 

        

