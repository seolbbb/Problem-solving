n, b = map(int, input().split())
s = ''
arr = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

while n:
    s += str(arr[n % b])
    n //= b

print(s[::-1])