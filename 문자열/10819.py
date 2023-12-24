# 백준 10819 - 차이를 최대로
import sys 
input = sys.stdin.readline 

N = int(input())
A = list(map(int, input().split()))
maximum = 0

def find_max():
    global maximum
    tmp = 0
    for j in range(len(A) - 1):
        tmp += abs(A[j] - A[j + 1])
    maximum = max(maximum, tmp)

def perm(k) :
    if (k == N):
        #print(A)
        find_max()
    for i in range(k, N):
        A[i], A[k] = A[k], A[i]
        perm(k+1)  
        A[i], A[k] = A[k], A[i]

perm(0)
print(maximum)