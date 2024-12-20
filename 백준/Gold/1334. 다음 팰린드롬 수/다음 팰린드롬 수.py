n = str(int(input()))
m = int(n)

if m < 9:
    n = str(m + 1)
    print(n)
    exit(0)
elif m == 9:
    n = '11'
    print(n)
    exit(0)

length = len(n)
half_length = (length + 1) // 2


first_half = n[:half_length]
if length % 2 == 0:
    palindrome = first_half + first_half[::-1]
else:
    palindrome = first_half + first_half[-2::-1]


if int(palindrome) > m:
    print(palindrome)
else:

    first_half = str(int(first_half) + 1)
    if len(first_half) > half_length:

        if length % 2 == 0:
            palindrome = first_half + first_half[::-1][1:]
        else:
            palindrome = first_half + first_half[::-1][2:]
    else:
        if length % 2 == 0:
            palindrome = first_half + first_half[::-1]
        else:
            palindrome = first_half + first_half[-2::-1]
    print(palindrome)