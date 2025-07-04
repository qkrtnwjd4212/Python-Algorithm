# 백준 1043 - 거짓말
import sys
input = sys.stdin.readline 

N, M = map(int, input().split()) # 사람, 파티
truth = list(map(int, input().split()))[1:] # 번호만 저장
parent = [i for i in range(N+1)] # 부모 테이블
for i in truth: # 진실을 아는 사람은 0번으로 통일 
    parent[i] = 0

parties = []

def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for _ in range(M): # 같은 파티에 참석한 사람들을 하나로 union
    party = list(map(int, input().split()))[1:] # 얘도 번호만 저장
    for i in range(len(party) - 1):
        union_parent(parent, party[i], party[i+1])
    parties.append(party)

answer = 0
for party in parties:
    know = False
    for i in range(len(party)):
        print()
        print(parent[i])
        if find_parent(parent, party[i]) == 0: # 파티 구성원의 부모가 0이면(진실을 아는애면)
            know = True
            break
    if not know:
        answer += 1

print(answer)