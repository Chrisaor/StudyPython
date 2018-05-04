def check_set_bits(n):
    for i in bin(n)[2:]:
        if i == '0':
            return 'NO'
    return 'YES'

t = int(input())
for i in range(t):
    N = input()
    n = int(input())
    print(check_set_bits(n))
