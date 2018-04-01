def total_count(key, arr):
    cnt = 0
    for i in range(len(arr)):
        if arr[i]//key == arr[i]/key:
            cnt += arr[i]//key
        else:
            cnt += arr[i]//key + 1
    return cnt

key = 3
arr = [5, 8, 10, 13, 6, 2]

t = int(input())
for i in range(t):
    N = list(map(int, input().split()))
    key = N[1]
    arr = list(map(int, input().split()))
    print(total_count(key, arr))
