t = int(input())

for _ in range(t):
    n = int(input())
    cnt = dict()
    ans = 1

    for _ in range(n):
        item, category = input().split()
        cnt[category] = cnt.get(category, 0) + 1
    
    for num in cnt.values():
        ans *= num+1
    
    ans -= 1

    print(ans)