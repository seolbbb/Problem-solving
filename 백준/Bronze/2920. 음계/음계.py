ascending = list(range(1,9))
descending = list(reversed(ascending))

A = list(map(int,input().split()))

if A == ascending:
    print('ascending')
elif A == descending:
    print('descending')
else:
    print('mixed')