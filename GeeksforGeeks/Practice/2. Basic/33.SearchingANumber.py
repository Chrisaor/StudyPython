def search_num(n, arr):
    try:
        return arr.index(n)+1
    except ValueError:
        return -1

t = int(input())
for i in range(t):
    N = list(map(int, input().split()))
    n = N[1]
    arr = list(map(int, input().split()))
    print(search_num(n, arr))
