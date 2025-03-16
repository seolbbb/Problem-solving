n, k = map(int, input().split())
st = sorted(list(map(int, input().split())), reverse=True)

print(st[k-1])