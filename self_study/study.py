arr = [[1, 2, 3, 4],
       [5, 6, 7, 8],
       [9, 10, 11, 12]]

# 시계 방향 90도 회전 ==============================================
# 1번 - 리스트 슬라이싱, zip 활용 (정사각형만 가능)
arr_90 = list(map(list, zip(*arr[::-1])))
# for row in arr_90:
#     print(*row)

# 2번 - 일반적 방법
m = len(arr) # 행 개수
n = len(arr[0]) # 열 개수
new_90 = [[0] * m for _ in range(n)] # 행, 열 개수 바뀜 주의!!
for i in range(m):
    for j in range(n):
        new_90[j][m-i-1] = arr[i][j] # 행, 열 바꿔서 들어감
# for row in new_90:
#     print(*row)

print()
# 시계 방향 180도 회전 ==============================================
# 1번 - 리스트 슬라이싱 활용 (정사각형일때만 가능)
arr_180 = [row[::-1] for row in arr[::-1]]
# for row in arr_180:
#     print(*row)

# 2번 - 일반적 방법
new_180 = [[0] * n for _ in range(m)]
for i in range(m):
    for j in range(n):
        new_180[m-i-1][n-j-1] = arr[i][j] # i, j 뒤바뀜 없음
for row in new_180:
    print(*row)

# 시계 방향 270도 회전 ==============================================
# 일반적 방법
new_270 = [[0] * m for _ in range(n)]
for i in range(m):
    for j in range(n):
        new_270[m-j-1][i] = arr[i][j]
