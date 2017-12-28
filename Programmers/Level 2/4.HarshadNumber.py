def Harshad(n):
    sumNum = 0
    ckN = n
    while ckN != 0:
        y = ckN % 10
        sumNum += y
        ckN = int(ckN/10)
    if n % sumNum == 0:
        return True
    else:
        return False

print(Harshad(57))

'''
def Harshad(n):
    return n % sum(int(x) for x in str(n)) == 0

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(Harshad(18))
'''
