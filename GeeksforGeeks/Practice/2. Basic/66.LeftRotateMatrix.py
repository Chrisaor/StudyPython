def left_rotate_matrix(arr,m,k):

    if k % 2 == 1:
        for i in range(m):
            arr[i] = arr[i][::-1]
    else:
        return ' '.join(map(str,arr))
    temp = list()
    for i in arr:
        temp += i
    # print(temp)
    return ' '.join(map(str,temp))

m = 2
n = 2
k = 1

str_arr = '1 2 3 4'
list_arr = list(map(int, str_arr.split(' ')))
arr = list()
print(list_arr)
for i in range(m):
    arr.append(list_arr[i*m:i*m+m])
print(left_rotate_matrix(arr,m,k))
