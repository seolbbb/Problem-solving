n = int(input())
topings = list(map(str, input().split()))
cheese = set()


for toping in topings:
    if len(toping) < 5 or toping[-6:] != 'Cheese':
        continue
    cheese.add(toping)

if len(cheese) >= 4:
    print('yummy')
else:
    print('sad')