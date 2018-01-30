def find_first_bit(n):
    bin_str = bin(n)[2:]
    bin_num = int(bin_str)
    for i in range(len(bin_str)):

        if bin_num == 0:
            return 0
        elif bin_num % 10 == 1:
            return i+1
        bin_num = bin_num // 10

t = int(input())
for i in range(t):
    n = int(input())
    print(find_first_bit(n))


# print(bin(366974))
