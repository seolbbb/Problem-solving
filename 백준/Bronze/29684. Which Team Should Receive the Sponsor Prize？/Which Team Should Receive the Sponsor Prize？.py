while True:
    n = int(input())
    if n == 0:
        break

    teams = list(map(int, input().split()))
    times = []

    for i in range(n):
        times.append((abs(2023-teams[i]), i+1))
    
    print(min(times)[1])