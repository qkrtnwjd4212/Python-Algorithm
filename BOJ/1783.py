# 백준 1783 - 병든 나이트
# 참고 : https://afterdawncoding.tistory.com/202
import sys 
input = sys.stdin.readline

n, m = map(int, input().split())
# move = [[1, 2], [2,1], [2,-1], [1,-2]] <- 최대 방문횟수만 구하면 되니까 좌표는 중요하지 않음!
# chess = [[0] * m for _ in range(n)]
# cur = [0, 0]

if n == 1:
    print(1)
elif n == 2:
    if m < 7:
        print((m+1) // 2)
    else:
        print(4)
elif n >= 3: # n이 3부터는 세로 길이 이동 제약 없음
    if m <= 4:
        print(m)
    elif m == 5 or m == 6:
        print(4)
    else: # 모든 방법을 다 쓰고 나서는 오른쪽으로 한칸만 이동해야 방문횟수 최대
        print(m-2)