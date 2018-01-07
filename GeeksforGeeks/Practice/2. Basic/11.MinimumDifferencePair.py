def minimumDiff(arr):
    sortedArr = sorted(arr)
    answer = abs(sortedArr[0] - sortedArr[1])
    for i in range(len(sortedArr)-1):
        diff = abs(sortedArr[i] - sortedArr[i+1])
        if answer > diff:
            answer = diff
    return answer


#
t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(minimumDiff(arr))
