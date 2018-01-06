t = int(input())

for i in range(t):
    n = int(input())
    numbers = [str(x) for x in input().split()]
    result = []
    for j in range(n):
        if numbers[j] not in result:
            result.append(numbers[j])
        else:
            result.remove(numbers[j])
