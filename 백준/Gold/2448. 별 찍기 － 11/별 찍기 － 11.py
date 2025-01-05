def star(num):
    if num == 3:
        return ["  *  ",
                " * * ",
                "*****"]


    stars = star(num//2)
    l = []
    for i in range(len(stars)):
        l.append(' ' * (num//2) + stars[i] + ' ' * (num//2))
    for s in stars:
        l.append(s + ' ' + s)
    return l

n = int(input())
print('\n'.join(star(n)))