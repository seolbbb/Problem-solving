n = int(input())
sold = sorted(list(map(int, input().split())))

ans = 1

for num in sold:
    if ans < num:
        break
    else:
        ans = num+1

print(ans)