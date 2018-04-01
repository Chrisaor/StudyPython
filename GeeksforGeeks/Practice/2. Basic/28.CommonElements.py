def common_elements(arr1, arr2, arr3):
    common_list = list()
    answer = list()
    for i in arr1:
        for j in arr2:
            print(i,j)
            if i == j:
                common_list.append(i)
                arr1.remove(i)
                arr2.remove(j)
                print(common_list)
    for i in common_list:
        for j in arr3:
            print(i,j)
            if i == j:
                answer.append(i)
                common_list.remove(i)
                arr3.remove(j)
    if len(answer)==0:
        return -1
    return ' '.join(map(str, answer))


arr1 = [1, 5, 10, 20, 40, 80]
arr2 = [6, 7, 20, 80, 100]
arr3 = [3, 4, 15, 20, 30, 70, 80, 120]

# t = int(input())
# for i in range(t):
#     n = list(map(int, input().split())
#     arr1 = list(map(int, input().split()))
#     arr2 = list(map(int, input().split()))
#     arr3 = list(map(int, input().split()))
print(common_elements(arr1, arr2, arr3))
