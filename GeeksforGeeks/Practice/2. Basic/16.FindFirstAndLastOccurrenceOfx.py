def find_idx(arr, num):
    first_occ = -1
    last_occ = -1
    for i in range(len(arr)):
        if first_occ < 0 and arr[i] == num:
            first_occ = i
            last_occ = i
        elif arr[i] == num:
            last_occ = i
    result = [first_occ, last_occ]
    if first_occ == -1:
        return -1
    else:
        return ' '.join(map(str,result))

t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    num = int(input())
    print(find_idx(arr, num))
