def nextLarger(n, arr):
    result = []
    for i in range(n):
        if i+1 == n:
           result.append(-1)
        else:
            for j in range(i, n):
                if j+1 == n:
                    result.append(-1)
                elif arr[j+1] > arr[i]:
                    result.append(arr[j+1])
                    break;

    answer = ' '.join(list(map(str, result)))
    return answer

t = int(input())
for x in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(nextLarger(n,arr))
