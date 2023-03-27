N = int(input())
num_list = list(map(int, input().split()))
find = int(input())
count = 0

# range() 함수를 쓰면 카운터 변수는 0부터 0,1,2,3,... 이렇게 순회함
# 리스트나 튜플을 사용하면 카운터 변수는 객체 안의 데이터들을 순회함
# list[0], list[1], ... 일케!!
for i in num_list:
    if (find == i):
        count += 1

# 다른 풀이 : print(n_list.count(v)) 사용
# 파이썬 리스트에는 어떤 값이 몇개있는지 세어주는 내장 메소드가 있었음...아놔
print(count)