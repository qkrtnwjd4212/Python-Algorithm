import sys

# def perm() :
#     global data, n, m, visited  
#     # base case
#     if (len(data) == m): 
#         print(' '.join(map(str, data)))  
#         return  
#     # recursive case
#     for i in range(1, n+1):
#         if (visited[i]):  
#             continue
#         visited[i] = 1  
#         data.append(i)  
#         perm()
#         data.pop() 
#         visited[i] = 0

# n, m = map(int, sys.stdin.readline().split())
# data = []  
# visited = [0] * (n+1) 
# num = [0] * m
 
# perm()

n, m = map(int, sys.stdin.readline().split())
data = []

def perm():
    if len(data)==m:
        print(' '.join(map(str, data)))
        return
    for i in range(1, n+1):
        if i not in data:  # 중복 체크 -> 배열 대신 파이썬 not in 연산자 사용하는거로 수정
            data.append(i)
            perm()
            data.pop()

perm()
