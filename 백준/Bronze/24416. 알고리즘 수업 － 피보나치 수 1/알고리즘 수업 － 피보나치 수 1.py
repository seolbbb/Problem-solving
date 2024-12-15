def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)
    
def fibonacci(n):
    cnt2 = 0
    f_arr = [0, 1]
    for i in range(2,n+1):
        num = f_arr[i-1] + f_arr[i-2]
        f_arr.append(num)
        cnt2 += 1
    return [f_arr[n], cnt2]


n = int(input())

print(fib(n), fibonacci(n)[1]-1)