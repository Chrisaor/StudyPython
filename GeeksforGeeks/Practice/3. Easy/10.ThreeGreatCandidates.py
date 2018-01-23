def three_great_candidates(arr):
    arr1 = sorted(arr)
    case1 = arr1[0]*arr1[1]*arr1[-1]
    case2 = arr1[-1]*arr1[-2]*arr1[-3]
    if case1 >= case2:
        return str(case1)
    else:
        return str(case2)


t = int(input())
for i in range(t):
    n = int(input());
    arr = list(map(int,input().split()))
    print(three_great_candidates(arr))
