n = int(input())
player = [-1 for _ in range(9)]
pine = 0
blue = 0

for _ in range(n):
    t, a, b = map(int, input().split())

    if 1 <= a <= 4:
        if player[a] == -1:
            pine += 100
        elif t-player[a] <= 10:
            pine += 150
        else:
            pine += 100
        player[a] = t
    else:
        if player[a] == -1:
            blue += 100
        elif t-player[a] <= 10:
            blue += 150
        else:
            blue += 100
        player[a] = t

print(pine, blue)