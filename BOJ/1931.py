# 백준 1931 - 회의실 배정
import sys
input = sys.stdin.readline

n = int(input())
meet = [] # 회의 시간

for i in range(n):
    a, b = map(int, input().rstrip().split())
    meet.append([a, b])

# 람다식 : 간단한 함수를 정의할 때 사용. (lambda 인자 : 표현식)
# sort()의 key 인자에는 함수 사용 가능
# key 2개 이상 사용 가능 -> 첫번째 key가 같을 때 두번째 key를 기준으로 비교
meet.sort(key=lambda x: (x[1],x[0])) # 1 회의종료시간, 2 회의시작시간을 우선순위로 정렬

count = 1 # 제일 먼저 끝나는 회의는 넣고 시작
end = meet[0][1]

for i in range(1, len(meet)): # 처음회의는 선택하고 1번 인덱스부터 시작!
    if end <= meet[i][0]: # 종료시간 <= 시작시간이면 회의 추가
        count += 1
        end = meet[i][1] # 종료 시간 업데이트

print(count)

