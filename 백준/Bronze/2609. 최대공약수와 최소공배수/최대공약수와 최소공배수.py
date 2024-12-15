x, y = map(int, input().split())
a = 1


for i in range(2, 10001):
    while x % i == 0 and y % i == 0:
        a *= i
        x //= i
        y //= i

print(a)
print(a*x*y)