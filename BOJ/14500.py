# 백준 14500 - 테트로미노
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

tetromino = [[(0,0), (0,1), (0,2), (0,3)], # I자 모양
             [(0,0), (1,0), (2,0), (3,0)],

             [(0,0), (0,1), (1,0), (1,1)], # 정사각형 모양

             [(0,0), (1,0), (2,0), (2,1)], # L자 모양
             [(0,0), (1,0), (1,1), (2,1)],
             [(0,0), (0,1), (0,2), (1,2)],
             [(0,0), (0,1), (1,1), (2,1)],
             [(0,0), (0,1), (0,2), (1,0)],
             [(0,1), (1,1), (2,1), (2,0)],
             [(1,0), (1,1), (1,2), (0,2)],
             [(0,0), (0,1), (1,0), (2,0)],
             [(0,0), (1,0), (1,1), (1,2)],
             [(0,1), (1,0), (1,1), (2,0)],
             [(0,1), (0,2), (1,0), (1,1)],
             [(0,0), (0,1), (1,1), (1,2)],

             [(0,0), (0,1), (0,2), (1,1)], # T자 모양
             [(0,1), (1,0), (1,1), (1,2)],
             [(0,1), (1,0), (1,1), (2,1)],
             [(0,0), (1,0), (1,1), (2,0)]]
max_value = 0

for i in range(n):
    for j in range(m):

        for t in tetromino:
            tmp_sum = 0
            flag = True
            for block in t:
                x, y = block
                if 0 <= i+x < n and 0 <= j+y < m:
                    tmp_sum += arr[i+x][j+y]
                else:
                    flag = False
                    break
            if flag:
                max_value = max(max_value, tmp_sum)

print(max_value)




