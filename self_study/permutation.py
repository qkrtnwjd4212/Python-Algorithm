import sys

def perm(k) :
    global data
    if (k == N):  # 집합 S가 공집합이고 전부 prefix string이면 
        print(data[:N])  # 리스트 전체 출력
    for i in range(k, N):
        data[i], data[k] = data[k], data[i] # k번째 값을 집합S의 앞으로 swap
        perm(k+1)  
        data[i], data[k] = data[k], data[i]  # 중요! swap했던걸 다시 돌려놔서 중복 순열 만들어지지 않게

N = int(sys.stdin.readline().strip())
data = list(range(1, N+1))
perm(0)