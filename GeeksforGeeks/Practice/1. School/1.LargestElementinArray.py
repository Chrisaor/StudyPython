def LargestElement(arr):
    return max(arr)

t = int(input())
for i in range(0, t):
    n = int(input())
    arr = map(int, input().split())
    print(LargestElement(arr))
