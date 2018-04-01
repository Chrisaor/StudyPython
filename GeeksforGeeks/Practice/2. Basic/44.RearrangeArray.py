def rearrange_array(arr):
    rearray = list()
    for i in range(len(arr)):
        if i % 2 == 0:
            num = arr.pop()
            rearray.append(num)
        else:
            num = arr[0]
            del arr[0]
            rearray.append(num)
    return ' '.join(map(str, rearray))


t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(rearrange_array(arr))
