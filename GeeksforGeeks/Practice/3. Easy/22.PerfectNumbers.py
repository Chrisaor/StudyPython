def perfect_numbers(n):
    sum = 0
    factors = list()
    for i in range(1,n+1):
        if n % i == 0:
            factors.append(i)
    factors = factors[:-1]
    for i in factors:
        sum += i
    if sum == n:
        return 1
    else:
        return 0

t = int(input())
for i in range(t):
    n = int(input())
    print(perfect_numbers(n))
