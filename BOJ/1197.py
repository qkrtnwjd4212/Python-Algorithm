# 백준 1197 - 최소 스패닝 트리
import sys
input = sys.stdin.readline 

V, E = map(int, input().split())
parent = [0] * (V+1)

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b 

edge = []
result = 0

for i in range(1, V+1):
    parent[i] = i

for _ in range(E):
    a, b, c = map(int, input().split()) # a->b 비용이 c
    edge.append((c, a, b))

edge.sort()

for i in edge:
    cost, a, b = i
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)
