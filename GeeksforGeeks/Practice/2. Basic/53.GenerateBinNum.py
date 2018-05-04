def bin_nums(n):
    temp = list()
    for i in range(1, n+1):
        temp.append(bin(i)[2:])
    return ' '.join(temp)


t = int(input())
for i in range(t):
    n = int(input())
    print(bin_nums(n))
