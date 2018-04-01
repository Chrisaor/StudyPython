def number_sparse(N):
    cnt1 = 0
    while N > 0:
        if N % 2 == 1:
            if cnt1 == 1:
                return 0
            else:
                cnt1 += 1
        else:
            cnt1 = 0
        N = N >> 1
    return 1

t = int(input())
for i in range(t):
    N = int(input())
    print(number_sparse(N))
