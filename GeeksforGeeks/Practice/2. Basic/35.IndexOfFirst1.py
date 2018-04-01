def index_of_1(arr):
    if 1 in arr:
        return arr.index(1)
    else:
        return -1

t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(index_of_1(arr))
