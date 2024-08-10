# 백준 1018 - 체스판 다시 칠하기
import sys
def input(): return sys.stdin.readline()

N, M = map(int, input().split()) # 세로 N, 가로 M
chess = []
count = []

for _ in range(N):
    chess.append(input())

for i in range(N-7):
    for j in range(M-7):
        start_W = 0
        start_B = 0

        for a in range(i,i+8):
            for b in range(j,j+8):
                if (a+b) % 2 == 0:
                    if chess[a][b] != 'W':
                        start_W += 1
                    if chess[a][b] != 'B':
                        start_B += 1
                else:
                    if chess[a][b] != 'B':
                        start_W += 1
                    if chess[a][b] != 'W':
                        start_B += 1
        
        count.append(min(start_B, start_W))
print(min(count))

    
