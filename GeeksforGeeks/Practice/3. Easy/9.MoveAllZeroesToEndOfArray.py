def moveAllZeroes(arr1):
    temp = []
    for i in range(len(arr1)):
        if arr1[i] == 0:
            temp = arr1[i]
            arr1.remove(arr1[i])
            arr1.append(0)

    return ' '.join(map(str,arr1))



t = int(input())
for i in range(t):
    n = int(input())
    arr1 = list(map(int, input().split()))
    print(moveAllZeroes(arr1))
