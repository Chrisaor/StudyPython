def Floor(arr, x):
    for i in range(len(arr)):
        print(i)
        if arr[0] == x:
            return 0
        elif arr[0] > x:
            return -1
        elif arr[i] > x:
            print('i-1', arr[i])
            return i-i
        elif arr[i] == x:
            print('i', arr[i])
            return i
    return i

t = int(input())
for i in range(t):
    N = list(map(int, input().split()))
    x = N[1]
    arr = list(map(int,input().split()))
    print(Floor(arr, x))
