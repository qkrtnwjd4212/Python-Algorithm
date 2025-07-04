# 백준 10825 - 국영수
import sys
input = sys.stdin.readline

N = int(input()) # 학생수
student = [] # 이름, 국, 영, 수
for _ in range(N):
    name, k, e, m = map(str, input().rstrip().split())
    k, e, m = int(k), int(e), int(m)
    student.append([name, k, e, m])

student.sort(key = lambda x: (-x[1], x[2], -x[3], x[0]))

for i in range(N):
    print(student[i][0])
