def find_min1_low(m, n, arr):
    numbers_of_1 = list()
    if sum(arr) == 0:
        return -1
    for i in range(m):
        numbers_of_1.append(sum(arr[n*i:n*(i+1)]))
    print(numbers_of_1)
    min_sum = sum(numbers_of_1)
    for i in numbers_of_1:
        print(min_sum)
        if i == 0:
            continue
        elif i < min_sum:
            min_sum = i
    print('len',len(numbers_of_1))
    return numbers_of_1.index(min_sum)

t = int(input())
for i in range(t):
    NM = list(map(int, input().split()))
    m = NM[0]
    n = NM[1]
    arr = list(map(int, input().split()))
    print(find_min1_low(m, n, arr))
