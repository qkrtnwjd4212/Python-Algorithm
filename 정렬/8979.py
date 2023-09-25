# 백준 8979 - 올림픽
import sys 
input = sys.stdin.readline 

N, K = map(int, input().split()) # 국가 수, 등수 궁금한 국가
medal = [list(map(int, input().split())) for _ in range(N)]
medal.sort(key = lambda x : (x[1], x[2], x[3]), reverse=True)

for i in range(N):
    if medal[i][0] == K:
        score = i+1
        idx = i

while True: # 공동n등 예외처리
    # 국가가 순서대로 들어온다는 보장없음 -> 인덱스로 K바로쓰면 안됨 ㅠㅠ
    if medal[idx][1] == medal[idx-1][1] and medal[idx][2] == medal[idx-1][2] and medal[idx][3] == medal[idx-1][3] and idx > 0:
        score -= 1
        idx -= 1
    else:
        break

print(score)

