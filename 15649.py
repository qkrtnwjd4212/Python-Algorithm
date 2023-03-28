import sys

def perm() :
    global data, n, m, visited  # 함수 밖에서 선언한 변수 사용 -> 전역변수로 선언
    # base case
    if (len(data) == m):  # m개만큼 넣었으면 
        print(' '.join(map(str, data)))  # data 안의 원소들 한칸씩 띄워서 출력
        return  # 백트래킹
    # recursive case
    for i in range(1, n+1):
        if (visited[i]):  # i번째 값이 이미 쓴거면 다음으로 넘어감
            continue

        visited[i] = 1  # 현재 원소 방문표시
        data.append(i)  # m개 넣을 때까지 재귀 호출
        perm()
        data.pop() # 썼던 값 빼기
        visited[i] = 0

n, m = map(int, sys.stdin.readline().split())
data = []  # 만들어진 수열을 넣을 빈 리스트
visited = [0] * (n+1)  # 방문 여부 확인 리스트

perm()  # 재귀 실행 