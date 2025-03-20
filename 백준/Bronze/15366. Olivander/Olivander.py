n = int(input())
ans = 'DA'

wands = sorted(list(map(int, input().split())), reverse=True)
boxes = sorted(list(map(int, input().split())), reverse=True)

for i in range(n):
    if wands[i] > boxes[i]:
        ans = 'NE'
        break

print(ans)