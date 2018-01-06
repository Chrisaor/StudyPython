def Reverse(arr):

    for i in range(len(arr)):
        result.append(arr.pop())
    return result

t = int(input())

for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(' '.join(Reverse(arr))
