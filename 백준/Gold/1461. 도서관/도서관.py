n, m = map(int, input().split())
books = list(map(int, input().split()))
ans = 0

minus = sorted([i for i in books if i < 0])
plus = sorted([i for i in books if i > 0], reverse = True)
plus_idx = 0
minus_idx = 0
bigger_p = 0

if minus and plus:
    if plus[0] > -minus[0]:
        bigger_p = 1
# 책의 위치 중 음수가 없는 경우
elif not minus:
    bigger_p = 1

# 책의 좌표값 음수, 양수로 나누어서 가장 절댓값이 큰 값을 ans에 더함.
if bigger_p:
    ans += plus[0]
    plus_idx += m
else:
    ans += -minus[0]
    minus_idx += m

while plus and plus_idx < len(plus):
    ans += (2*plus[plus_idx])
    plus_idx += m

while minus and minus_idx < len(minus):
    ans += -(2*minus[minus_idx])
    minus_idx += m

print(ans)