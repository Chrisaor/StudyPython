def sum_of_two_large_numbers(n, m):
    digit_max = 0
    digit_sum = 0
    num_max = n
    sum_of_two = n+m
    while num_max != 0:
        num_max = num_max // 10
        digit_max += 1
    while sum_of_two != 0:
        sum_of_two = sum_of_two //10
        digit_sum += 1
    if digit_max == digit_sum:
        return n+m
    else:
        return n

t = int(input())
for i in range(t):
    N = list(map(int, input().split()))
    n = N[0]
    m = N[1]
    print(sum_of_two_large_numbers(n,m))
