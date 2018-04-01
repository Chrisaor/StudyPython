def number_of_occurrence(number, arr):
    cnt = 0
    for i in range(len(arr)):
        if arr[i] == number:
            cnt +=1
    if cnt == 0:
        return -1
    else:
        return cnt


t = int(input())

for i in range(t):

    N = list(map(int, input().split()))
    n = N[0]
    number = N[1]
    arr = list(map(int, input().split()))
    print(number_of_occurrence(number, arr))
