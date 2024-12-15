n = int(input())

if n % 5 == 0:
    print(n // 5)
else:
    bag = 0
    while n > 0:
        n -= 3
        bag += 1
        if n % 5 == 0:
            bag += n // 5
            print(bag)
            break
        elif n == 1 or n == 2:
            print(-1)
            break
        elif n == 0:
            print(bag)
            break