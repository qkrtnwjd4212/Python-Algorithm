# 백준 1197 - 최소 스패닝 트리
import sys
input = sys.stdin.readline 

V, E = map(int, input().split())
parent = [0] * (V+1)
edge = []
result = 0

for i in range(1, V+1):
    parent[i] = i

for _ in range(E):
    a, b, c = map(int, input().split()) # a->b 비용이 c
    edge.append((c, a, b))

edge.sort()

def find_parent(parent, x):
    root = x
    while parent[root] != root:
        root = parent[root]

    while x != root:
        parent_x = parent[x]
        parent[x] = root
        x = parent_x
    return root

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a == b:
        return

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for i in edge:
    cost, a, b = i
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)
