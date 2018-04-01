def distribution(m, arr):
    arr2 = sorted(arr)
    arr_list = list()
    min_list = list()
    for i in range(len(arr2)):
        j = 0
        j = i+m
        arr3 = arr2[i:j]
        if len(arr3) == m:
            arr_list.append(arr3)
            min_list.append(arr3[-1]-arr3[0])
    return min(min_list)

t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    m = int(input())
    print(distribution(m, arr))
