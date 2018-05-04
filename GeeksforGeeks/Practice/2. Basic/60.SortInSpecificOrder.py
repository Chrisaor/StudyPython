def sort_in_specific_order(arr):
    temp_even = list()
    temp_odd = list()
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            temp_even.append(arr[i])
        else:
            temp_odd.append(arr[i])
    return ' '.join(map(str, sorted(temp_odd,reverse=True)+sorted(temp_even)))

t = int(input())
for i in range(t):
    n = input()
    arr = list(map(int, input().split()))
    print(sort_in_specific_order(arr))
