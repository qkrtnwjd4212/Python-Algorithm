# 백준 11403 - 경로 찾기
import sys 
input = sys.stdin.readline 
INF = int(1e9)

n = int(input())
graph = [list(map(int, (input().split()))) for _ in range(n)]

# 입력 데이터에서 0인 값 INF로 바꾸기
for i in range(n):
    for j in range(n):
        if graph[i][j] == 0:
            graph[i][j] = INF
# 플로이드 워셜 알고리즘 수행
for k in range(n):
    for a in range(n):
        for b in range(n):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
# INF면 0으로, 아니면 1로 출력
for i in range(n):
    for j in range(n):
        if graph[i][j] == INF:
            print(0, end=' ')
        else:
            print(1, end=' ')
    print()