def Epoint(n, arr):
    for i in range(n):
        midIdx = i
        if sum(arr[0:midIdx]) == sum(arr[midIdx+1:]):
            return midIdx+1
    return -1

t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(Epoint(n, arr))
