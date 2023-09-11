# 백준 2816 - 디지털 티비
import sys 
input = sys.stdin.readline

N = int(input())
channel = [str(input().rstrip()) for _ in range(N)]
btn = []

a, b = channel.index('KBS1'), channel.index('KBS2')
p = 0 # 포인터

while channel[p] != 'KBS1': # KBS1까지 채널 내리기
    btn.append(1)
    p += 1
for _ in range(p): 
    btn.append(4)

channel.remove('KBS1')
channel.insert(0, 'KBS1') # 리스트에서 KBS1 채널을 앞으로

p = 0
while channel[p] != 'KBS2':
    btn.append(1)
    p += 1
for _ in range(p-1):
    btn.append(4)

for i in btn:
    print(i, end='')