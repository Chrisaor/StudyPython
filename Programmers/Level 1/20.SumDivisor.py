def sumDivisor(num):
    answer = 0
    for i in range(1, num+1):
        if (num % i) == 0:
            answer += i
    return answer


print(sumDivisor(12))

'''<Clean Code>
def sumDivisor(num):
    return num + sum([i for i in range(1, (num // 2) + 1) if num % i == 0])
'''
