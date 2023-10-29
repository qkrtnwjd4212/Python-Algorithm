# 백준 1966 - 프린터 큐
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    # 문서 개수, 궁금한 문서가 현재 몇번째인지
    N, M = map(int, input().split())
    q = list(map(int, input().split()))

    count, idx = 0, M
    while q: # 큐가 빌때까지
        if idx != 0:
            if q[0] != max(q):
                q.append(q.pop(0))
                idx -= 1
                count += 1
            else:
                q.pop(0)
                idx -= 1
                count += 1
        else:
            if q[0] != max(q):
                idx += len(q) -1
                q.append(q.pop(0))
                count += 1
            else:
                print(count)
                break

