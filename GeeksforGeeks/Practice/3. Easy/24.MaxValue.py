def max_value(arr):
    temp = list()

    for i in range(len(arr)):
        value = 0
        for j in range(i+1,len(arr)):
            value = abs((arr[i]-i) - (arr[j]-j))
            temp.append(value)

    return max(temp)

t = int(input())
for i in range(t):
    n = input()
    arr = list(map(int, input().split()))
    print(max_value(arr))
