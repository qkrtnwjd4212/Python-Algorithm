# 백준 9663 - N-Queen
import sys
input = sys.stdin.readline
n = int(input())

visited = [0] * n
cnt = 0

def check(cur_row):
    for row in range(cur_row):
        if visited[row] == visited[cur_row] or cur_row - row == abs(visited[cur_row] - visited[row]):
            return False
    return True

def dfs(row):
    global cnt

    if row == n:
        cnt += 1
    else:
        for col in range(n):
            visited[row] = col
            if check(row):
                dfs(row + 1)

dfs(0)
print(cnt)