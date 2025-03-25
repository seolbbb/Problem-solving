t = int(input())

for _ in range(t):
    text = list(input().split())

    for word in text:
        print(word[::-1], end=' ')
    print()