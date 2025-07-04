import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))

# A.sort()
# B.sort(reverse=True)
# sum = 0
# for i in range(N):
#     sum += A[i] * B[i]
# print(sum)

sum = 0
for i in range(N):
    a = min(A)
    b = max(B)
    sum += a * b 
    A.pop(A.index(a))
    B.pop(B.index(b))

print(sum)

