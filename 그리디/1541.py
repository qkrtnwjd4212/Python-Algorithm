# 백준 1541 - 잃어버린 괄호
import sys 
input = sys.stdin.readline

str = input().rstrip().split('-') # '-' 기준으로 나눠서 입력받기

for i in range(len(str)):
    # '+' 기준으로 나눈 뒤 다 더해서 str 리스트에 다시 저장
    sum = 0
    tmp = list(map(int, str[i].split('+')))
    for j in tmp:
        sum += j
    str[i] = sum

result = str[0]
for i in range(1, len(str)): # 리스트를 돌면서 차례로 빼기
    result -= str[i]

print(result)
