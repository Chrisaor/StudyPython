def count_elements(arr1, arr2):
    result = list()
    for i in range(len(arr1)):
        cnt = 0
        for j in range(len(arr2)):
            if arr1[i]>=arr2[j]:
                cnt += 1
        result.append(str(cnt))

    return ','.join(result)



# arr1 = [95, 39, 49, 20, 67, 26, 63]
# arr2 = [77, 96, 81, 65, 60, 36, 55]
t = int(input())
for i in range(t):
    N = int(input())
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    print(count_elements(arr1,arr2))
