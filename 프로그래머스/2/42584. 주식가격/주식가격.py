def solution(prices):
    n = len(prices)
    ans = [0] * n
    stack = []  # 아직 하락이 확정되지 않은 인덱스들

    for i, p in enumerate(prices):
        # 현재 p가 더 작아졌다면(하락), 그동안 쌓여있던 인덱스들의 종료를 확정
        while stack and prices[stack[-1]] > p:  # '>' (같은 값은 하락 아님)
            j = stack.pop()
            ans[j] = i - j
        stack.append(i)

    # 끝까지 하락 안 온 것들 처리
    while stack:
        j = stack.pop()
        ans[j] = (n - 1) - j

    return ans