def merge_array(arr1, arr2):
    return ' '.join(map(str, sorted(arr1+arr2,reverse=True)))

t = int(input())
for i in range(t):
    N = input()
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    print(merge_array(arr1, arr2))
