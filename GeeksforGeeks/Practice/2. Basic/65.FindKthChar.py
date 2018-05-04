def find_kth_char(m,k,n):
    bin_m = bin(m)[2:]
    print(bin_m)
    temp = list()
    for i in range(n):
        print(i+1)
        for j in list(bin_m):
            # print('j : ',j)
            if j == '0':
                temp.append('01')
                # print(j,'01추가')
            elif j == '1':
                temp.append('10')
                # print(j,'10추가')
        bin_m = ''.join(temp)
        temp = list()
        print(bin_m)
    return list(bin_m)[k]

# t = int(input())
# for i in range(t):
#     N = list(map(int, input().split()))
#     m = N[0]
#     k = N[1]
#     n = N[2]
m = 42
k = 47
n = 8
print(find_kth_char(m,k,n))
