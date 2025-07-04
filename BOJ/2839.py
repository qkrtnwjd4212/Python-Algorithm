# 백준 2839 - 설탕 배달

# N = int(input())
# tmp_N = N
# count = 0

# while (N>0):
#     if N<3:
#         count = -1
#         break
#     elif N>=5:
#         N -= 5
#         count += 1
#     else:
#         N -= 3
#         count += 1

# if tmp_N % 3 == 0 and count == -1:
#     count = tmp_N // 3 


# print(count)

N = int(input())
count = 0

while N > 0:
    if N % 5 == 0:
        count += N // 5
        break
    N -= 3
    count += 1

if N < 0:
    count = -1

print(count)