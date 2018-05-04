def closest_zero(arr):
    result = list()
    answer = list()
    sum = 0
    if len(arr) == 2:
        return ' '.join(list(map(str, arr)))
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            sum = arr[i] + arr[j]
            result.append(abs(sum))
            if len(result) >= 2 and min(result) == abs(sum):
                answer = list()
                answer.append(str(arr[i]))
                answer.append(str(arr[j]))
    return ' '.join(sorted(answer))

t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(closest_zero(arr))
