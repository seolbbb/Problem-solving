num = 0

for i in range(3):
    x = input()
    if x.isdigit():
        num = int(x) + (3-i)

if num % 3 == 0 and num % 5 == 0:
    print("FizzBuzz")
elif num % 3 == 0:
    print("Fizz")
elif num % 5 == 0:
    print("Buzz")
else:
    print(num)