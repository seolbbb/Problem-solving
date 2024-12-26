T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    price = list(map(int, input().split()))
    profit = 0
    max_price = 0

    # Iterate from the end to the beginning
    for i in range(n - 1, -1, -1):
        if price[i] > max_price:
            max_price = price[i]
        profit += max_price - price[i]

    print('#%d %d' % (test_case, profit))