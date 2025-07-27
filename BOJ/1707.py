# 백준 1707 - 이분 그래프
import sys
input = sys.stdin.readline
from collections import deque

k = int(input().strip())

for _ in range(k):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v + 1)]
    group = [0] * (v + 1)

    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)


    # setrecursionlimit는 미리 메모리를 할당해두기 때문에 값을 크게 설정하면 메모리초과가 날 수 있음.
    # 문제의 제한사항을 확인하고 그에 맞춰서 설정하기!!
    # 문제의 정점 개수가 최대 2만개 -> 재귀 깊이도 20000 까지만!!!
    def dfs(idx, group, prev):
        group[idx] = prev  # 현재 노드 그룹 지정

        for node in graph[idx]:
            if group[node] == prev:  # 인접 노드랑 같은 그룹 -> 실패
                return False
            elif group[node] == 0:  # 아직 방문 안한 곳일때 -> 반대그룹으로 할당
                if not dfs(node, group, -prev):
                    return False
        return True

    # def bfs(start):
    #     q = deque()
    #     q.append(start)
    #
    #     while q:
    #         now = q.popleft()
    #         for next in graph[now]:
    #             if group[next] == 0:
    #                 group[next] = -group[now]
    #                 q.append(next)
    #             elif group[next] == group[now]:
    #                 return False
    #     return True


    ans = True
    for i in range(1, v + 1):
        if group[i] == 0:
            if not dfs(i, group, 1):
                ans = False
                break
            # if not bfs(i):
            #     ans = False
            #     break

    print("YES" if ans else "NO")




