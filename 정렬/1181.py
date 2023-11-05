# 백준 1181 - 단어 정렬
import sys
input = sys.stdin.readline

N = int(input())
word = [input().rstrip() for _ in range(N)]
word = list(set(word)) # 집합을 이용해 중복 제거
word.sort() # 사전순으로 먼저 정렬
word.sort(key=lambda x: (len(x))) # 문자의 길이를 기준으로 다시 정렬

for i in word:
    print(i)
