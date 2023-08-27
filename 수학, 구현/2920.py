# 백준 2920 - 음계
import sys 
input = sys.stdin.readline

piano = list(map(int, input().split()))

asc = 0
dsc = 0

for i in range(8):
    if i+1 == piano[i]:
        asc += 1
    elif 8-i == piano[i]:
        dsc += 1
    
if asc == 8:
    print("ascending")
elif dsc == 8:
    print("descending")
else:
    print("mixed")