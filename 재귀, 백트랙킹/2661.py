# 백준 2661 - 좋은 수열
import sys
input = sys.stdin.readline

def check_good():
    for i in range(1, (len(good)//2) + 1):
        # print('good:', good)
        # print(good[-i:], good[-2*i-1:-i])
        if good[-i:] == good[-2*i : -i]:
            return 0
    return 1

def backtracking(level):
    if not check_good():
        return 0
    
    if level == N:
        print(''.join(map(str,good)))
        return 1
        
    for i in range(1,4):
        good.append(i)
        if backtracking(level+1) != 0: #일케하니까 틀림 뭐가다른지잘모르겟음;
            return 1
        #if backtracking(level+1): # 반환값 없어야함!!!!
            #return 1
        good.pop()

N = int(input())
good = []
backtracking(0)