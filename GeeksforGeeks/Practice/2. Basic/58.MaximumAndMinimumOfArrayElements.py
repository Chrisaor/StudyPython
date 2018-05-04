def max_min_array(arr):
    return ' '.join([str(max(arr)), str(min(arr))])

t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(max_min_array(arr))
