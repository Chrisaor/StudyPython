def alone_in_couple(N, arr):
    temp = list()
    for i in range(N):
        if arr[i] not in temp:
            temp.append(arr[i])
        else:
            temp.remove(arr[i])
    return temp[0]


t = int(input())
for i in range(t):
    N = int(input())
    arr = list(map(int, input().split()))
    print(alone_in_couple(N, arr))
