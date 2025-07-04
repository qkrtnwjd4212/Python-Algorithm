# 백준 1157 - 단어 공부
import sys 
input = sys.stdin.readline

str = input().rstrip().lower()
dic = {}

for i in str:
    dic[i] = 0
for i in str:
    dic[i] += 1

max_num = max(dic.values()) # dic[max(dic)]는 key의 최대값을 찾음 (알파벳중에 제일 큰거..)
cnt = 0
for i in dic:
    if dic[i] == max_num:
        cnt += 1

if cnt > 1:
    print("?")
else:
    print(max(dic, key=dic.get).upper())

# 딕셔너리의 max()는 key를 기준으로 value를 출력함
# value를 기준으로 최대값을 찾고싶으면 .value() 함수 사용
# key를 출력하고 싶으면 key=dict.get 속성 추가