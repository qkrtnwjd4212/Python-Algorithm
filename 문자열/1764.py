# 백준 1764 - 듣보잡
import sys
input = sys.stdin.readline

# N, M = map(int, input().rstrip().split()) # 듣, 보
# nothear = [input().rstrip() for _ in range(N)]
# notsee = [input().rstrip() for _ in range(M)]
# total = nothear + notsee

# dbj = [] # 듣보잡 ㅋㅋ
# for i in total:
#     if total.count(i) == 2:
#         dbj.append(i)
# dbj = set(dbj)

# print(len(dbj))
# for i in dbj:
#     print(i)

N, M = map(int, input().rstrip().split()) # 듣, 보
nothear = {input().rstrip() for _ in range(N)}
notsee = {input().rstrip() for _ in range(M)}

# intersection : 교집합(&) 
dbj = list(nothear.intersection(notsee))
dbj.sort()

print(len(dbj))
for i in dbj:
    print(i)

