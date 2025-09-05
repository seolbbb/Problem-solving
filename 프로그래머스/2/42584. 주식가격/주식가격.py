# 처음에는 stack의 뒤에서부터 탐색하는 걸 생각함
# 뒤에서부터 탐색하면서 시간을 1초씩 더하고, 현재 나온 숫자보다 작은 수가 나온 시점을 기록해서 빼 줌
# 예시)
# [1, 2, 3, 2, 1, 3]

# 3 : 0초
# 1 : 1초
# 2 : 2초 - 1초(1초에 2보다 작은 수 나옴)
# 3 : 3초 - 2초(2초에 3보다 작은 수 나옴)
# 2 : 4초 - 1초(1초에 2보다 작은 수 나옴)
# 1 : 5초

# 근데 현재 가격보다 작은 수가 나온 시점을 탐색하는 과정에서 시간 복잡도 O(n)
# stack 탐색 loop 안에 들어가니까 시간 복잡도 O(n^2)이 나와서 이 방법은 포기함


def solution(prices):
    n = len(prices)
    ans = [0] * n
    stack = []

    for i, p in enumerate(prices):
        while stack and prices[stack[-1]] > p:
            j = stack.pop()
            ans[j] = i - j
        stack.append(i)

    while stack:
        j = stack.pop()
        ans[j] = (n - 1) - j

    return ans