# 백준 1759 - 암호 만들기
import sys 
input = sys.stdin.readline

L, C = map(int, input().split()) # 암호 길이, 전체 문자 개수
word = list(map(str, input().split()))
word.sort()
answer = []

def str_count(str): # 모음, 자음 개수 세서 조건에 맞는지 확인
    vow = "aeiou"
    v_cnt, c_cnt = 0, 0

    for i in str:
        if i in vow:
            v_cnt += 1
        else:
            c_cnt += 1
    
    if v_cnt >= 1 and c_cnt >= 2:
        return True
    else:
        return False

def password(start, level):
    if level == L and str_count(answer):
        print(''.join(answer))
    else:
        for i in range(start, C):
            answer.append(word[i])
            password(i+1, level+1)
            answer.pop()

password(0,0)


# 순열 코드 이용...하려다 못푼거
# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
# N = len(word)
# def str_order(str): # 문자열 알파벳이 증가하는 순서인지
#     for i in range(len(str) - 1):
#         if str[i] > str[i+1]:
#             return False
#     return True

# def str_count(str):
#     vow = "aeiou"
#     v_cnt, c_cnt = 0, 0

#     for i in str:
#         if i in vow:
#             v_cnt += 1
#         else:
#             c_cnt += 1
    
#     if v_cnt >= 1 and c_cnt >= 2:
#         return True
#     else:
#         return False

# def perm(k) :
#     global word
#     if k == N and str_order(word[:L]) and str_count(word[:L]):  # 집합 S가 공집합이고 전부 prefix string이면 
#         print("".join(word[:L]))  

#     for i in range(k, N):
#         word[i], word[k] = word[k], word[i] # k번째 값을 집합S의 앞으로 swap
#         perm(k+1)  
#         word[i], word[k] = word[k], word[i]  # 중요! swap했던걸 다시 돌려놔서 중복 순열 만들어지지 않게

# word.sort()
# perm(0)
