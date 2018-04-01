def binary_search(list, item):
    low = 0
    high = len(list)-1

    while low <= high:
        mid = (low+high) / 2
        guess = list[mid]

        if guess == item:
            return mid
        elif guess > item:
            high = mid -1
        else:
            low = mid + 1
    return None

my_list = [1,3,5,7,9]

print(binary_search(my_list, 3)) # =>1
print(binary_search(my_list, -1)) # => None


# def binary_search(item, arr):
#     low = 0
#     high = len(arr)-1
#     guess = 0
#
#     while guess != item:
#         mid = (low+high)//2
#         guess = arr[mid]
#         if item not in arr:
#             return -1
#         elif guess == item:
#             return arr.index(guess)
#         elif guess > item:
#             low = mid + 1
#         elif guess < item:
#             high = mid - 1
#
#
# print(binary_search(3, [1,2,4,5,6]))
