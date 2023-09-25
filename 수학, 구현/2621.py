# 백준 2621 - 카드게임
import sys 
input = sys.stdin.readline 

color = {'R':0, 'B':0, 'Y':0, 'G':0}
num = [0 for _ in range(10)] # 1~9까지 (index 0은 안씀)
for _ in range(5):
    a, b = map(str, input().rstrip().split())
    color[a] += 1
    num[int(b)] += 1

def check_straight(): # 모두 연속하는 수인지 검사
    tmp = 1
    for i in range(1, 9):
        if num[i+1] == num[i]:
            tmp += 1
        else: tmp = 1 # 다른 값이 나오면 초기화
        if tmp == 5: # 이거도 카운트한 뒤에 검사하고 출력하기 ㅠ
            return i+1
    else: return 0

def check_max(): # 카드 번호(인덱스)의 최대값 출력
    tmp_max = 0
    for i in range(1, 10):
        if num[i] != 0 and i > tmp_max:
            tmp_max = i
    return tmp_max

# pair, arr = 0, []
# def check_cards(): # 페어 개수 검사
#     global pair, arr
#     for i in range(1, 10):
#         if num[i] == 2:
#             pair += 1
#             arr.append(i) # 8번 규칙용
#     print(arr)
#     return pair
pair, arr = 0, []
for i in range(1, 10):
    if num[i] == 2:
        pair += 1
        arr.append(i)


if 5 in color.values() and check_straight(): # 1번 규칙 - 스트레이트 플러쉬
    print(900 + check_straight())
elif 4 in num: # 2번 규칙 - 포카드
    print(800 + num.index(4))
elif 3 in num and 2 in num: # 3번 규칙 - 풀하우스
    print(700 + (10 * num.index(3)) + num.index(2))
elif 5 in color.values(): # 4번 규칙 - 플러쉬
    print(600 + check_max())
elif check_straight(): # 5번 규칙 - 스트레이트
    print(500 + check_straight())
elif 3 in num: # 6번 규칙 - 쓰리카드
    print(400 + num.index(3))

# elif check_cards() == 2: # 7번 규칙 - 투페어
#     print(300 + (10 * max(arr)) + min(arr))
# 이거 조건을 함수로 검사하니까 함수가 두번 실행돼서 원페어인데도 arr에 두번 들어감!
# elif check_cards() == 1: # 8번 규칙 - 원페어 
#     print(200 + num.index(2))

elif pair == 2: # 7번 규칙 - 투페어
    print(300 + (10 * max(arr)) + min(arr))
elif pair == 1: # 8번 규칙 - 원페어
    print(200 + num.index(2))
else: # 9번 규칙
    print(100 + check_max())
