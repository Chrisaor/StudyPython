def LongestName(arr):
    answer = ""
    for i in range(len(arr)):
        if len(answer) < len(arr[i]):
            answer = arr[i]
    return answer

t = int(input())
for i in range(0, t):
    n = int(input())
    arr = []
    for j in range(n):
        arr.append(input())
    print(LongestName(arr))
