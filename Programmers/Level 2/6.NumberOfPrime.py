def numberOfPrime(n):
    result = []
    for i in range(2,n+1):
        nPrime = []
        for j in range(1,i+1):
            if i % j == 0:
                nPrime.append(j)
        if len(nPrime) == 2:
            result.append(j)
    return len(result)

print(numberOfPrime(5))
