import sys

N = int(sys.stdin.readline())
data = [[0] * 4 for _ in range(N)]  # name, kor, eng, math

for i in range(N):
    data[i]  = sys.stdin.readline().split()

data = sorted(data, key=lambda x: (-int(x[1]), int(x[2]), -int(x[3])))
for i in range(N):
    print(data[i][0])

#, x[2], -x[3]