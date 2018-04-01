def binary_search(item, arr):
    low = 0
    high = len(arr)-1
    arr = sorted(arr)
    print(arr)
    while low <= high:
        mid = (low+high) // 2
        guess = arr[mid]
        print('mid:',mid,'guess:', guess)
        print('low:',low,'high:', high)
        if item not in arr:
            return -1

        elif item == guess:
            return mid
        elif item > guess:
            low = mid + 1
        else:
            high = mid - 1


print(binary_search(3, [1,5,6,7,8,9,3]))
