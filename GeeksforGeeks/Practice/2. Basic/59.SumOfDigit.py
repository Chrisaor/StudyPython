def sum_of_digits(n):
    count = 0
    while n > 0:
        count += (n%10)
        n = n//10
    return count

t = int(input())
for i in range(t):
    n = int(input())
    print(sum_of_digits(n))
