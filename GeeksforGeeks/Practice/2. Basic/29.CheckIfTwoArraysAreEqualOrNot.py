def equal_arr(arr1, arr2):
    if sorted(arr1) == sorted(arr2):
        return 1
    else:
        return 0


t = int(input())
for i in range(t):
    n = int(input())
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    print(equal_arr(arr1,arr2))
