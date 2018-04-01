def majority_element(arr):
    list1 = list()
    for i in arr:
        list1.append(arr.count(i))

    majority = arr[list1.index(max(list1))]
    print(majority)
    if max(list1) > len(arr)/2:
        return majority
    else:
        return 'NO Majority Element'


t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(majority_element(arr))
