def swap_kth(a, arr):
    temp = list()
    temp.append(arr[a-1])
    arr[a-1] = arr[-a]
    arr[-a] = temp[0]
    return ' '.join(map(str, arr))


t = int(input())
for i in range(t):
    N = list(map(int, input().split()))
    a = N[1]
    arr = list(map(int, input().split()))
    print(swap_kth(a,arr))
