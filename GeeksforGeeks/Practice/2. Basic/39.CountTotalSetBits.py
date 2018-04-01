def count_total(N):
    cnt = 0
    for i in range(1,N+1):
        cnt += bin(i)[2:].count('1')
    return cnt

t = int(input())
for i in range(t):
    N = int(input())
    print(count_total(N))
