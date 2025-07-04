# 백준 3009 - 네 번째 점
import sys 
input = sys.stdin.readline 

# x, y 나눠서 입력받으면 꼭짓점 분류할때 편함!
rec = [] # x = [], y = []
for _ in range(3):
    a, b = map(int, input().split())
    rec.append([a, b])

x1, x2 = min(rec[0][0], rec[1][0], rec[2][0]), max(rec[0][0], rec[1][0], rec[2][0])
y1, y2 = min(rec[0][1], rec[1][1], rec[2][1]), max(rec[0][1], rec[1][1], rec[2][1])

# 직사각형 -> 각 x, y좌표가 두번씩 나와야함. 한번씩 카운트된 좌표 조합하면 그게 마지막 꼭짓점!
rec_list = [[x1, y1], [x1, y2], [x2, y1], [x2, y2]]
for i in rec_list:
    if i in rec:
        continue
    else:
        print(i[0], i[1])