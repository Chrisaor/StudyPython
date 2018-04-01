def frequency_elements(N, arr):
    e_list = list()
    for i in range(len(arr)):
        e_list.append(0)

    for i in range(len(arr)):
        e_list[arr[i]-1] += 1

    return ' '.join(map(str, e_list))

t = int(input())
for i in range(t):
    N = int(input())
    arr = list(map(int, input().split()))
    print(frequency_elements(N, arr))
