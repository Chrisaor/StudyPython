def selectionSort(arr):
    findMin = [0]
    for i in range(len(arr)):
        findMin[0] = arr[i]
        print('target idx : ', i, 'arr1[i] : ', arr[i])
        for j in range(i+1,len(arr)):
            if findMin[0] > arr1[j]:
                findMin[0] = arr1[j]
                print('check this : ', arr[j],'find another Min :',findMin)
        arr[arr.index(findMin[0])] = arr[i]
        arr[i] = findMin[0]
        print(arr)
    return arr


arr1 = [9,1,12,6,8,4,3,2,0,7,11,13,15]
print(selectionSort(arr1))


# def selectionSort(x):
# 	length = len(x)
# 	for i in range(length-1):
# 	    indexMin = i
# 		for j in range(i+1, length):
# 			if x[indexMin] > x[j]:
# 				indexMin = j
#         if x[i] != x[indexMin]:
# 		      x[i], x[indexMin] = x[indexMin], x[i]
# 	return x
