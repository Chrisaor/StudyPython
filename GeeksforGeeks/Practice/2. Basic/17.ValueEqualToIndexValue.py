def value_index_equal(arr):
    result = []
    for i in range(len(arr)):
        idx = i+1
        if arr[i] == idx:
            result.append(idx)
    if result != []:
        return ' '.join(map(str, result))
    else :
        return "Not Found"

t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(value_index_equal(arr))
