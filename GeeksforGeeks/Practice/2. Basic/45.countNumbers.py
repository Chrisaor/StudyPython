def count_numbers(N):
    cnt = 0
    num_list = list('12345')
    for i in range(1,N+1):
        if set(str(i)) < set(num_list):
            cnt += 1
    return cnt

t = int(input())
for i in range(t):
    N = int(input())
    print(count_numbers(N))
