# 백준 10809 - 알파벳 찾기
import sys 
input = sys.stdin.readline

word = input().rstrip()

for i in range(ord('a'), ord('z')+1): # 알파벳 a부터 z까지 반복
    if chr(i) in word:
        print(word.find(chr(i)), end=' ') # find() : 문자열에서 특정 문자의 첫 등장 위치를 반환
    else:
        print(-1, end=' ')