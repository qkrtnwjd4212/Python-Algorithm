# 15650 : 15649랑 동일, 대신 수열이 오름차순 이어야함!!
import sys

n, m = map(int, sys.stdin.readline().split())
data = []

def perm(start):
    if (len(data) == m): # m개만큼 뽑았으면
        print(' '.join(map(str, data))) # 수열 출력하고 return
        return  
    # 오름차순 수열만 만들기 위해, 파라미터로 전달받은 값부터 n까지 반복함 
    # (start보다 작은 값이 data에 들어가면 역전쌍 만들어짐)
    for i in range(start, n+1):
        if i not in data: # data 에 없으면
            data.append(i)  # 넣고
            perm(i + 1) # 다음 값 재귀 호출
            data.pop()

perm(1)
