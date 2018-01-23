def maximum_product(arr):
    result = []
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            result.append(arr[i]*arr[j])
    return str(max(result))

t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(maximum_product(arr))
