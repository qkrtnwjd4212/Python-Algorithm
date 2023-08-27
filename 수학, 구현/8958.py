# 백준 8958 - OX퀴즈
import sys 
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    score = 0 # 각 문제의 점수
    sum = 0 # 점수의 합
    ans = list(map(str, input().rstrip()))

    for i in ans:
        if i == 'O':
            score += 1
            sum += score
        else:
            score = 0
    print(sum)
