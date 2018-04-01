def rotate_array(n, arr):
    temp = arr[:n]
    arr = arr[n:]
    answer = arr+temp
    return ' '.join(map(str, answer))

t = int(input())
for i in range(t):
    N = list(map(int, input().split()))
    n = N[1]
    arr = list(map(int, input().split()))
    print(rotate_array(n, arr))
