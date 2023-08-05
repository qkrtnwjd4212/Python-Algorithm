# 백준 2470 - 두 용액
import sys
input = sys.stdin.readline

n = int(input().rstrip())
ph = list(map(int, input().rstrip().split()))


# 시간초과남ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅋㅋ
# 이중 for문으로 그리디 -> O(N^2)
# min = abs(ph[0])
# num = [0, 0]
# for i in range(n):
#     for j in range(i+1, n):
#         tmp = abs(ph[i] + ph[j])
#         if min > tmp:
#             min = tmp
#             num = [ph[i], ph[j]]

# print(num[0], num[1])

ph.sort()
start, end = 0, n-1
min = abs(ph[start] + ph[end])
res = [ph[start], ph[end]] # 이거!!!!!!!!!!!!!!

# two pointer -> O(N)
while start < end:
    tmp = ph[start] + ph[end]
    if min > abs(tmp):
        min = abs(tmp)
        res = [ph[start], ph[end]]

    if ph[0] >= 0: # 다 양수일 때
        res = [ph[0], ph[1]]
        break
    elif ph[n-1] <= 0: # 다 음수일 때
        res = [ph[n-2], ph[n-1]]
        break

    if tmp < 0:
        start += 1
    elif tmp > 0:
        end -= 1
    else:
        break


print(res[0], res[1])