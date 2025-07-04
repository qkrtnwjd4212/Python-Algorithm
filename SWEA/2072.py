T = int(input())
for test_case in range(1, T + 1):
    ans = 0
    num_list = list(map(int, input().split()))

    for num in num_list:
        if num % 2 != 0:
            ans += num

    print(f"#{test_case} {ans}")