def pythagorean(arr):
    sq_arr = [i*i for i in arr]
    for i in range(len(sq_arr)):
        for j in range(i+1,len(sq_arr)):
            print(i,j)
            sum = sq_arr[i]+sq_arr[j]
            if sum in sq_arr:
                return 'Yes'
    return 'No'

t = int(input())
for i in range(t):
    n = input()
    arr = list(map(int, input().split()))
    print(pythagorean(arr))
