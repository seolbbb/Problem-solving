def hannoi(a,b,n):
    if n == 1:
        print(a,b)
        return

    hannoi(a,6-a-b,n-1)
    print(a,b)
    hannoi(6-a-b,b,n-1)

n = int(input())
print(2**n - 1)
hannoi(1,3,n)