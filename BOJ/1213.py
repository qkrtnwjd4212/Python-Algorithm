# 백준 1213 - 팰린드롬 만들기
name = list(input())
name.sort()

# 알파벳별로 딕셔너리 만들기
cnt = {}
for i in name:
    cnt[i] = 0
for i in name:
    cnt[i] += 1

odd_num = 0 # 홀수인 알파벳 개수
odd = '' # 홀수인 알파벳 
half = '' 
for i in cnt:
    if cnt[i] % 2 == 1:
        odd_num += 1
        odd = i
    half += i * (cnt[i] // 2)


if odd_num > 1:
    print("I'm Sorry Hansoo")
else:
    print(half + odd + half[::-1])