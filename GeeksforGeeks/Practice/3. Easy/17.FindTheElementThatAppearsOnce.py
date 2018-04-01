def appears_once(arr):
    for i in arr:
        if arr.count(i) == 1:
            return i
    return -1


t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(appears_once(arr))
