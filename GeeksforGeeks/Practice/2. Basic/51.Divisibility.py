def divisibility(n):
    str_n = str(n)
    sum = 0
    for i in str_n:
        sum += int(i)
    if n % sum == 0:
        return 1
    return 0

t = int(input())
for i in range(t):
    n = int(input())
    print(divisibility(n))
