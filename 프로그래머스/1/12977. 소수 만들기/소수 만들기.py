def solution(nums):
    answer = 0
    primes = [1 for _ in range(3000)]
    for i in range(2, int(3000 ** 0.5)):
        if primes[i] == 1:
            j = 2
            while i*j < 3000:
                primes[i*j] = 0
                j += 1
    
    for i in range(len(nums)-2):
        for j in range(i+1, len(nums)-1):
            for k in range(j+1, len(nums)):
                if primes[nums[i]+nums[j]+nums[k]] == 1:
                    answer += 1
    return answer