def union_two(arr1, arr2):
    for i in range(len(arr2)):
        if arr2[i] not in arr1:
            arr1.append(arr2[i])
    return ' '.join(map(str, sorted(arr1)))

t = int(input())
for i in range(t):
    N = input()
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    print(union_two(arr1, arr2))
