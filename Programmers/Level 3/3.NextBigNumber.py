def nextBigNumber(n):
    numOne = 0
    for i in str(bin(n))[2:]:
        if i == "1":
            numOne += 1
    numBiggerOne = 0
    while numBiggerOne != numOne:
        n += 1
        numBiggerOne = 0
        for j in str(bin(n))[2:]:
            if j == "1":
                numBiggerOne += 1
    return n


print(nextBigNumber(244291))

'''<Clean Code>
def nextBigNumber(n):
    num1 = bin(n).count('1')
    while True:
        n = n + 1
        if num1 == bin(n).count('1'):
            break
    return n

#아래 코드는 테스트를 위한 출력 코드입니다.
print(nextBigNumber(78))
'''
