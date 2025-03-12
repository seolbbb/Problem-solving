n = int(input())
papers = sorted(list(map(int, input().split())), reverse=True)
ans = 0

for i in range(n, -1, -1):
    higher = 0
    lower = 0

    for paper in papers:
        if paper >= i and higher < i:
            higher += 1
        elif paper <= i:
            lower += 1

    if higher >= i and (lower + higher) == n:
        ans = i
        break

print(ans)