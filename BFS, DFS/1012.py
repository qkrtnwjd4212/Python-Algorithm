# 1012 - 유기농 배추 (연결 요소의 개수)
import sys 
sys.setrecursionlimit(10000) 

# dfs
def dfs(x,y):
    if x<0 or x>=n or y<0 or y>=m:
        return False
    if graph[x][y] == 1:
        graph[x][y] = 0
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False

t = int(input()) # 테스트 케이스 개수
for _ in range(t):
    m, n, k = map(int, input().split()) # 가로, 세로, 배추개수

    graph = [[0] * m for _ in range(n)] # mxn 크기의 리스트
    for i in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1

    count = 0
    for i in range(n):
        for j in range(m):
            if dfs(i,j) == True:
                count += 1
    print(count)
