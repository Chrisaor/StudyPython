def product_array_puzzle(arr):
    prod = 1
    temp = list()
    result = list()
    for i in range(len(arr)):
        temp = arr[:i] + arr[i+1:]
        for j in temp:
            prod *= j
        result.append(str(prod))
        prod = 1
    return ' '.join(result)

t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(product_array_puzzle(arr))
