def set_bits(n):
    i = 0
    while n != 0:
        if n & 1 == 1:
            i += 1
        n = (n >> 1)
    return i


t = int(input())
for i in range(t):
    n = int(input())
    print(set_bits(n))
