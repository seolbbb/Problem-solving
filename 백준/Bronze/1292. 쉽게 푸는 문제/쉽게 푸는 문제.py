a, b = map(int, input().split())
arr = []
n = 1

while len(arr) <= b:
    for _ in range(n):
        arr.append(n)
    n += 1

print(sum(arr[a-1:b]))