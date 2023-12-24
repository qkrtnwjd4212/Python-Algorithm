# 백준 3649 - 로봇 프로젝트
import sys 
input = sys.stdin.readline 

while True:
    try:
        x = int(input()) * 10000000 # 구멍 너비 (cm->nm)
        n = int(input()) # 레고 조각의 수
        lego = [] # 레고 조각의 길이, nm
        for i in range(n):
            lego.append(int(input()))
        lego.sort()

        ok = [] # 구멍을 막을 수 있을 때의 레고 조각
        flag = False

        # 이진탐색
        start, end = 0, n-1
        while start < end:
            tmp = lego[start] + lego[end]
            if tmp > x:
                end -= 1
            elif tmp < x:
                start += 1
            else:
                ok.append([lego[start], lego[end]])
                flag = True
                break

        ok.sort(key=lambda x: abs(x[0] - x[1]))

        if flag == False:
            print("danger")
        else:
            print("yes", min(ok[-1]), max(ok[-1]))
    except:
        break

    
