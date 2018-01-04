def findLeader(n, arr):
    answer = []
    for i in range(n):
        if arr[i] > max(arr[i+1:]):
            answer.append(arr[i])
        elif arr[i] == arr[n]:
            answer.append(arr[i])
    return answer


t = int(input())
for i in range(t):
    n = int(input())
    arr = map(int, input().split())
    print(findLeader(n, arr))
