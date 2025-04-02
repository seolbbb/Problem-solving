n = int(input())
ans = 0

if n < 100:
    ans = n
else:
    ans = 99
    for i in range(100, n+1):
        num = str(i)
        gap = int(num[0]) - int(num[1])
        flag = 0

        for j in range(1, len(num)-1):
            if gap != int(num[j]) - int(num[j+1]):
                break
            flag = 1
        
        ans += flag


print(ans)