def FibonacciNumber(n):
    numArr = [1, 1]
    if n == 1 or n == 2:
        return 1
    else:
        for i in range(2,n):
            num = numArr[i-1] + numArr[i-2]
            numArr.append(num)
        return numArr[n-1]

# t = int(input())
# for i in range(t):
#     n = int(input())
n = 44
print(FibonacciNumber(n))
# 1 2 3 4 5 6  7  8  9 10
# 1 1 2 3 5 8 13 21 34 55
