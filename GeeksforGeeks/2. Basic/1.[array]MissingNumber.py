def MissingNumber(n, arr):
    sumOfN = n*(n+1)/2
    return sumOfN - sum(arr)

t = int(input())
for i in range(t):
    n = int(input())
    arr = map(int, input().split())
    print(MissingNumber(n, arr))



# t = int(input().strip())
# for i in range(t):
#     n = int(input().strip())
#     l = map(int, input().strip().split(' '))
#     print(n*(n+1) // 2 - sum(l))
#
#
# def find_missing(N, C):
#     return list(set(range(1, N+1)) - set(C))[0]
#
# num_tests = int(input())
# for i in range(num_tests):
#     N = int(input())
#     C = list(map(int, input().split()))
#
#     print(find_missing(N, C))
