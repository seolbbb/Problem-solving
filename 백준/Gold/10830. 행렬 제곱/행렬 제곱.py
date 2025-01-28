def matmul(a, b):
    c = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            s = 0
            for k in range(n):
                s += a[i][k]*b[k][j]
            c[i][j] = s % 1000
    return c

def matpow(base, exp):
    result = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        result[i][i] = 1

    while exp > 0:
        if exp & 1:
            result = matmul(result, base)
        base = matmul(base, base)
        exp //= 2

    return result

n, b = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

res = matpow(arr, b)
for i in range(n):
    print(*res[i])