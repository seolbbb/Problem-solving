n = int(input())
i = 0
num = 665
ans = 0

while i < n:
    if '666' in str(num):
        i += 1
        ans = num
        num += 1
    else:
        num += 1

print(ans)